from decimal import Decimal as number
from settings import Settings
import all_functions
import log
class basic_functions:
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
    def function(self, function, roundTo = int(Settings["FunctionsRoundTo"])):
        #Addictional Functions#
        factorial = all_functions.factorial
        sin = all_functions.sin
        cos = all_functions.cos
        tg = all_functions.tg
        ctg = all_functions.ctg
        ln = all_functions.ln
        lg = all_functions.lg
        logb = all_functions.logb
        #######################
        function = self.function_cleaner(function)
        #log.log("function", function)
        return self.OutputConvert(eval(function), roundTo)     
    def function_cleaner(self, function: str):
        return function.replace("\n", "").replace(" ", "")
    def variable_replace(self, STRING: str, FROM: str, TO: str):
        try:
            if Settings["NumberType"] == "Decimal":
                return str(STRING).replace(FROM, "number(" + str(TO) + ")")
            if Settings["NumberType"] == "Float":
                return str(STRING).replace(FROM, "float(" + str(TO) + ")")
        except:
            return "Expected: Error (variable_replace)"
    def solve_function(self, function, variables: dict, roundTo = int(Settings["FunctionsRoundTo"])):
        for key in variables.keys():
            function = self.variable_replace(function, key, variables[key])
        #log.log("function", function)
        return self.function(function, roundTo)