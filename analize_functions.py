import basic_functions
from settings import Settings, RoundTo
from decimal import Decimal as number
import decimal
import log

class analize_functions:
    base_math = basic_functions.basic_functions()
    dx = 0
    inf = number("infinity")
    def __init__(self):
        self.SetDX()
        log.log("set DX", self.dx)
    def DifferencialX(self, function, x):
        x = self.base_math.OutputConvert(x)
        dx = self.SetDXLocal(RoundToDX=RoundTo)
        dx = self.base_math.OutputConvert(dx)
        #log.error("x + dx", str(self.base_math.OutputConvert(x + dx)) + " " + str(type(x+dx)))
        #log.error("dx", str(dx)+ " " + str(type(dx)))
        #log.error("x", str(x)+ " " + str(type(x)))
        fx2 = self.base_math.solve_function(function, variables={"x": x + dx})
        #log.error("x + dx", x + dx)
        #log.error("DF(x) -> fx2", fx2)
        fx1 = self.base_math.solve_function(function, variables={"x": x})
        #log.error("DF(x) -> fx1", fx1)
        return self.base_math.OutputConvert(fx2 - fx1)
    def DerivedX(self, function, x):
        dx = self.SetDXLocal(RoundToDX=RoundTo)
        fx = self.DifferencialX(function, x)
        return self.base_math.OutputConvert(fx/dx)
    def IntegralXStandart(self, function, a, b, IntegralDX = 3):
        dx = self.SetDXLocal(RoundToDX=IntegralDX)
        result = 0
        while a <= b:
            temp = self.base_math.solve_function(function, variables={"x": a})
            result += self.base_math.OutputConvert(temp)*dx
            a += dx
        return self.base_math.OutputConvert(result)
    def LimitX(self, function, x0, SolveAccuracy = RoundTo, DeepLimit=False):
        try:
            result = self.base_math.solve_function(function, variables={"x": x0})
            return self.base_math.OutputConvert(result)
        except:
            if DeepLimit == True:
                result1 = self.base_math.solve_function(function, variables={"x": x0 - self.dx})
                result2 = self.base_math.solve_function(function, variables={"x": x0 + self.dx})
                if abs(result1 - result2) < self.SetDXLocal(SolveAccuracy):
                    return self.base_math.OutputConvert(result1)
                else:
                    result1add = self.base_math.solve_function(function, variables={"x": x0 - self.dx/2})
                    result2add = self.base_math.solve_function(function, variables={"x": x0 + self.dx/2})
                    result1 = self.base_math.OutputConvert(result1)
                    result2 = self.base_math.OutputConvert(result2)
                    result1add = self.base_math.OutputConvert(result1add)
                    result2add = self.base_math.OutputConvert(result2add)
                    if result2add > result2:
                        return [result1*self.inf, result2*self.inf]
                    else:   
                        return [result1, result2]
            else:
                return None
    def SetDX(self, RoundToDX = 3):
        self.dx = self.base_math.OutputConvert(number("0." + "0"*(RoundToDX - 1) + "1"))
    def SetDXLocal(self, RoundToDX = 3):
        return self.base_math.OutputConvert(number("0." + "0"*(RoundToDX - 1) + "1"))
    def Summa(self, function, n_start, n_end, variables_addictional = {}):
        variables = {"n": 0}
        for key in variables_addictional.keys():
            variables[key] = variables_addictional[key]
        result = 0
        iterations = 0
        temp = 0.1
        if n_start <= n_end:
                while (n_start <= n_end and abs(temp) >= self.dx) and iterations <= 15:
                    variables["n"] = n_start
                    #log.log("solve_function",self.base_math.solve_function(function, variables))
                    temp = self.base_math.solve_function(function, variables)
                    #log.log("temp", temp)
                    result += temp
                    n_start += 1
                    iterations += 1
        else:
            while (n_start >= n_end and abs(temp) >= self.dx) and iterations <= 15:
                variables["n"] = n_start
                #log.log("solve_function", self.base_math.solve_function(function, variables))
                temp = self.base_math.solve_function(function, variables)
                #log.log("temp", temp)
                result += temp
                n_start -= 1
                iterations += 1
        #log.log("iterations", iterations)
        #print("!!!!!!!!!!!!!!!",result)
        return self.base_math.OutputConvert(result)