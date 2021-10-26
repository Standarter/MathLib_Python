import basic_functions
from settings import Settings
from decimal import Decimal as number
import log

class analize_functions:
    base_math = basic_functions.basic_functions()
    def Summa(self, function, n_start, n_end, variables_addictional = {}):
        variables = {"n": 0}
        for key in variables_addictional.keys():
            variables[key] = variables_addictional[key]
        result = 0
        iterations = 0
        temp = 0.1
        if n_start <= n_end:
                while (n_start <= n_end and temp != 0) or iterations <= 3:
                    variables["n"] = n_start
                    #log.log("solve_function",self.base_math.solve_function(function, variables))
                    temp = self.base_math.solve_function(function, variables)
                    #log.log("temp", temp)
                    result += temp
                    n_start += 1
                    iterations += 1
        else:
            while (n_start >= n_end and temp != 0) or iterations <= 3:
                variables["n"] = n_start
                #log.log("solve_function", self.base_math.solve_function(function, variables))
                temp = self.base_math.solve_function(function, variables)
                #log.log("temp", temp)
                result += temp
                n_start -= 1
                iterations += 1
            log.log("iterations", iterations)
        #print("!!!!!!!!!!!!!!!",result)
        return self.base_math.OutputConvert(result)