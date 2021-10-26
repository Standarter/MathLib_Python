from decimal import Decimal as number
from settings import Settings
import all_functions
import log
class basic_functions:
    def OutputConvert(self, Number):
        Number = str(round(Number, int(Settings["FunctionsRoundTo"])))
        if Settings["NumberType"] == "Float":
            return float(Number)
        if Settings["NumberType"] == "Decimal":
            return number(Number)
    def function(self, function):
        #Addictional Functions#
        factorial = all_functions.factorial
        #######################
        function = self.function_cleaner(function)
        #log.log("function", function)
        return self.OutputConvert(eval(function))
            
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
    def solve_function(self, function, variables: dict):
        for key in variables.keys():
            function = self.variable_replace(function, key, variables[key])
        #log.log("function", function)
        return self.function(function)