from settings import Settings
from decimal import Decimal as number
from analize_functions import analize_functions
import all_functions
import log
class math_functions:
    def OutputConvert(self, Number):
        Number = str(round(Number, int(Settings["FunctionsRoundTo"])))
        if Settings["NumberType"] == "Float":
            return float(Number)
        if Settings["NumberType"] == "Decimal":
            return number(Number)
    def RadianInputConvert(self, x):
        #print(self.OutputConvert((x % all_functions.pi) + 2*all_functions.pi))
        return self.OutputConvert((x % all_functions.pi) + 2*all_functions.pi)
    def __init__(self):
        all_functions.pi = 3.1415926535
        all_functions.e = 2.7182818284
        if Settings["TrigMethod"] == "math":
            import math
            def sin(x):
                return self.OutputConvert(math.sin(x))
            def cos(x):
                return self.OutputConvert(math.cos(x))
            def tg(x):
                return self.OutputConvert(math.sin(x)/math.cos(x))
            def ctg(x):
                return self.OutputConvert(math.cos(x)/math.sin(x))
            all_functions.sin = sin
            log.log("loaded", "sin (math)", level=3)
            all_functions.cos = cos
            log.log("loaded", "cos (math)", level=3)
            all_functions.tg = tg
            log.log("loaded", "tg (math)", level=3)
            all_functions.ctg = ctg
            log.log("loaded", "ctg (math)", level=3)
        if Settings["TrigMethod"] == "numpy":
            import numpy
            def sin(x):
                return self.OutputConvert(numpy.sin(x))
            def cos(x):
                return self.OutputConvert(numpy.cos(x))
            def tg(x):
                return self.OutputConvert(numpy.sin(x)/numpy.cos(x))
            def ctg(x):
                return self.OutputConvert(numpy.cos(x)/numpy.sin(x))
            all_functions.sin = sin
            log.log("loaded", "sin (numpy)", level=3)
            all_functions.cos = cos
            log.log("loaded", "cos (numpy)", level=3)
            all_functions.tg = tg
            log.log("loaded", "tg (numpy)", level=3)
            all_functions.ctg = ctg
            log.log("loaded", "ctg (numpy)", level=3)
        if Settings["TrigMethod"] == "taylor":
            analize = analize_functions()
            def sin(x, iterations = 10):
                formula = """
                ( (-1)**(n) * x**(2*n+1) ) /
                ( factorial(2*n + 1) )
                """
                return self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
            def cos(x, iterations = 10):
                formula = """
                ( (-1)**(n) * x**(2*n) ) /
                ( factorial(2*n) )
                """
                return self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
            def tg(x, iterations = 10):
                return self.OutputConvert(sin(x, iterations)/cos(x, iterations))
            def ctg(x, iterations = 10):
                return self.OutputConvert(cos(x, iterations)/sin(x, iterations))
            all_functions.sin = sin
            log.log("loaded", "sin (taylor)", level=3)
            all_functions.cos = cos
            log.log("loaded", "cos (taylor)", level=3)
            all_functions.tg = tg
            log.log("loaded", "tg (taylor) (slow)", level=3)
            all_functions.ctg = ctg
            log.log("loaded", "ctg (taylor) (slow)", level=3)
        if Settings["FactorialMethod"] == "standart":
            def factorial(x):
                if x > 0:
                    #log.log("X", x)
                    result = 1
                    for i in range(1, int(x) + 1, 1):
                        #log.log("i", i)
                        result *= i
                        #log.log("result", result)
                    return self.OutputConvert(result)
                if x == 0:
                    return self.OutputConvert(1)
            all_functions.factorial = factorial
            log.log("loaded", "factorial (standart)", level=3)