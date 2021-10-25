from decimal import Decimal as number
from settings import Settings
class basic_functions:
    def function(self, function):
        try:
            return eval(function)
        except ZeroDivisionError:
            return "Expected: ZeroDivizion (function)"
        except Exception:
            return "Expected: Error (function)"
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
        return self.function(function)