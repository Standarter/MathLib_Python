from settings import Settings
from decimal import Decimal as number
import decimal
from analize_functions import analize_functions
import all_functions
import log
import math as python_math
import numpy
import math
class math_functions:
    basicDecimal = type(number(0.0))
    basicFloat = type(float(0.0))
    basicInt = type(int(0))
    def OutputRound(self, Number, roundTo=int(Settings["FunctionsRoundTo"])):
        return round(Number, roundTo)
    def OutputConvert(self, Number, roundTo = int(Settings["FunctionsRoundTo"])):
        #log.error("OutputConvert", Number)
        Number = self.OutputRound(Number)
        if Settings["NumberType"] == "Float":
            return float(Number)
        if Settings["NumberType"] == "Decimal":
            return number(Number)
    def RadianInputConvert(self, x):
        return self.OutputConvert((x % all_functions.pi) + 2*all_functions.pi)
    def ArcRadianConvert(self, x):
        return self.OutputConvert((x % 2*all_functions.pi))
    def __init__(self):

        # CONSTANTS #
        analize = analize_functions()
        all_functions.pi = self.OutputConvert(3.1415926535)
        all_functions.e = self.OutputConvert(2.7182818284)
        # ######### #

        # Define functions
        def logb(a, b):
            return python_math.log(b)/python_math.log(a)
        def sin_math(x):
            return self.OutputConvert(math.sin(x))
        def cos_math(x):
            return self.OutputConvert(math.cos(x))
        def tg_math(x):
            return self.OutputConvert(math.sin(x)/math.cos(x))
        def ctg_math(x):
            return self.OutputConvert(math.cos(x)/math.sin(x))
        def sin_numpy(x):
            return self.OutputConvert(numpy.sin(x))
        def cos_numpy(x):
            return self.OutputConvert(numpy.cos(x))
        def tg_numpy(x):
            return self.OutputConvert(numpy.sin(x)/numpy.cos(x))
        def ctg_numpy(x):
            return self.OutputConvert(numpy.cos(x)/numpy.sin(x))
        def sin_numpy(x):
            return self.OutputConvert(numpy.sin(x))
        def cos_numpy(x):
            return self.OutputConvert(numpy.cos(x))
        def tg_numpy(x):
            return self.OutputConvert(numpy.sin(x)/numpy.cos(x))
        def ctg_numpy(x):
            return self.OutputConvert(numpy.cos(x)/numpy.sin(x))
        def sin_taylor(x, iterations = 100):
            formula = """
            ( (-1)**(n) * x**(2*n+1) ) /
            ( factorial(2*n + 1) )
            """
            return self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
        def cos_taylor(x, iterations = 100):
            formula = """
            ( (-1)**(n) * x**(2*n) ) /
            ( factorial(2*n) )
            """
            return self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
        def tg_taylor(x, iterations = 10):
            return self.OutputConvert(sin(x, iterations)/cos(x, iterations))
        def ctg_taylor(x, iterations = 10):
            return self.OutputConvert(cos(x, iterations)/sin(x, iterations))
        def arcsin_taylor(x, iterations = 20):
            formula = """
            ( factorial(2*n) * x**(2*n+1) ) /
            ( 4**n * factorial(n)**2 * (2*n+1) )
            """
            result = self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
            return self.ArcRadianConvert(result)
        def arccos_taylor(x, iterations = 13):
            formula = """
            ( factorial(2*n) * x**(2*n+1) ) /
            ( 4**n * factorial(n)**2 * (2*n+1) )
            """
            result = self.OutputConvert(analize.Summa(formula, 0, iterations, variables_addictional={"x": self.RadianInputConvert(x)}))
            return self.ArcRadianConvert(result)
        def sh_standart(x):
            e = all_functions.e
            return self.OutputConvert((e**x-e**(-x))/2)
        def ch_standart(x):
            e = all_functions.e
            return self.OutputConvert((e**x+e**(-x))/2)
        def th_standart(x):
            return self.OutputConvert(sh_standart(x)/ch_standart(x))
        def cth_standart(x):
            return self.OutputConvert(ch_standart(x)/sh_standart(x))
        def sch_standart(x):
            return self.OutputConvert(1/ch_standart(x))
        def csch_standart(x):
            return self.OutputConvert(1/sh_standart(x))
        def power(x, y):
            if Settings["NumberType"] == "Float":
                return self.OutputConvert(float(x)**float(y))
            if Settings["NumberType"] == "Decimal":
                return self.OutputConvert(number(x)**number(y))
        if Settings["LogMethod"] == "standart":
            all_functions.ln = python_math.log
            log.log("loaded", "log (math)", level=3)
            all_functions.lg = python_math.log10
            log.log("loaded", "lg (math)", level=3)
            all_functions.logb = logb
            log.log("loaded", "logb (math)", level=3)
        if Settings["TrigMethod"] == "math":
            all_functions.sin = sin_math
            log.log("loaded", "sin (math)", level=3)
            all_functions.cos = cos_math
            log.log("loaded", "cos (math)", level=3)
            all_functions.tg = tg_math
            log.log("loaded", "tg (math)", level=3)
            all_functions.ctg = ctg_math
            log.log("loaded", "ctg (math)", level=3)
        if Settings["TrigMethod"] == "numpy":
            all_functions.sin = sin_numpy
            log.log("loaded", "sin (numpy)", level=3)
            all_functions.cos = cos_numpy
            log.log("loaded", "cos (numpy)", level=3)
            all_functions.tg = tg_numpy
            log.log("loaded", "tg (numpy)", level=3)
            all_functions.ctg = ctg_numpy
            log.log("loaded", "ctg (numpy)", level=3)
        if Settings["TrigMethod"] == "taylor":
            all_functions.sin = sin_taylor
            log.log("loaded", "sin (taylor)", level=3)
            all_functions.cos = cos_taylor
            log.log("loaded", "cos (taylor)", level=3)
            all_functions.tg = tg_taylor
            log.log("loaded", "tg (taylor) (slow)", level=3)
            all_functions.ctg = ctg_taylor
            log.log("loaded", "ctg (taylor) (slow)", level=3)
        if Settings["FactorialMethod"] == "standart":
            def factorial(x):
                if x > 0:
                    result = 1
                    for i in range(1, int(x) + 1, 1):
                        result *= i
                    return self.OutputConvert(result)
                if x == 0:
                    return self.OutputConvert(1)
            all_functions.factorial = factorial
            log.log("loaded", "factorial (standart)", level=3)
        all_functions.arcsin = arcsin_taylor
        log.log("loaded", "arcsin (taylor)", level=3)
        all_functions.arccos = arccos_taylor
        log.log("loaded", "arccos (taylor)", level=3)
        all_functions.power = power
        log.log("loaded", "power (standart)", level=3)