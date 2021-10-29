from basic_functions import *
import all_functions
class math_analisys:
    ############################
    base_math = basic_functions()
    ############################
    dx = 0
    ############################
    def __init__(self):
        self.set_dx()
        settings.dx = self.dx
        all_functions.diff = self.diff
    def set_dx(self, roundto=settings.default_function_round):
        one = self.base_math.to_decimal_number("1")
        ten = self.base_math.to_decimal_number("10")
        self.dx = one/ten**roundto
        #print(self.dx)
    def set_local_dx(self, roundto=settings.default_function_round):
        one = self.base_math.to_decimal_number("1")
        ten = self.base_math.to_decimal_number("10")
        return one/ten**roundto
    def diff(self, formula, x0):
        dy2 = self.base_math.default_function(formula, variables={"x": x0 + self.dx})
        dy1 = self.base_math.default_function(formula, variables={"x": x0})
        result = (dy2-dy1)/self.dx
        return self.base_math.to_decimal_number_with_round(result)
    def integrate(self, formula, a, b, roundto = settings.default_function_round):
        dx = self.set_local_dx(3 if roundto > 3 else roundto)
        c = 1 if a <= b else -1
        if b < a:
            a, b = b, a
        a = self.base_math.to_decimal_number_with_round(a)
        b = self.base_math.to_decimal_number_with_round(b)
        result = self.base_math.to_decimal_number_with_round("0")
        while a < b:
            result += self.base_math.default_function(formula, variables={"x": a})*dx
            a += dx
        return result*c