from basic_functions import *
from math_analisys import *
import random
class numbers_methods:
    base_math = basic_functions()
    analisys = math_analisys()
    def __init__(self):
        all_functions.newton_method = self.newton_method
    def newton_method(self, formula, x0, iterations = 100):
        one = self.base_math.default_function(formula, variables={"x": x0})
        two = self.analisys.diff(formula, x0)
        count = 0
        try:
            while iterations > 0 and abs(one/two) > self.analisys.dx:
                try:
                    one = self.base_math.default_function(formula, variables={"x": x0})
                    two = self.analisys.diff(formula, x0)
                    x0 -= one/two
                    #print("One/Two", one/two)
                    iterations -= 1
                    count += 1 
                except:
                    #print(count)
                    return self.base_math.to_decimal_number_with_round(x0)
            #print(count)
            return self.base_math.to_decimal_number_with_round(x0)
        except:
            return self.base_math.to_decimal_number_with_round(x0)