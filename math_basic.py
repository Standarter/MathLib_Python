from basic_functions import *
import all_functions
class math_basic:
    base_math = basic_functions()
    def __init__(self):
        all_functions.sin = self.sin
        all_functions.cos = self.cos
        all_functions.tg = self.tg
        all_functions.ctg = self.ctg
        all_functions.factorial = self.factorial
    def factorial(self, x):
        result = self.base_math.to_decimal_number("1")
        x = self.base_math.to_decimal_number(x)
        #print(x)
        for i in range(1, int(x) + 1):
            result *= self.base_math.to_decimal_number(i)
            #print(result)
        return self.base_math.to_decimal_number_with_round(result)
    def sin(self, x, iterations = settings.iterations_for_sin):
        x = self.base_math.to_decimal_number_with_round(x)
        result = self.base_math.to_decimal_number_with_round("0")
        #print("x", x)
        for i in range(int(iterations)):
            i = self.base_math.to_decimal_number_with_round(i)
            #print("i",i, type(i))
            one = self.base_math.to_decimal_number_with_round("-1")**i
            #print("one",one, type(one))
            two = x**(self.base_math.to_decimal_number_with_round("2")*i+self.base_math.to_decimal_number_with_round("1"))
            #print("two",two, type(two))
            three = self.factorial(self.base_math.to_decimal_number_with_round("2")*i+self.base_math.to_decimal_number_with_round("1"))
            #print("three", three, type(three))
            result += self.base_math.to_decimal_number_with_round(one*two/three)
        return result
    def cos(self, x, iterations = settings.iterations_for_cos):
        x = self.base_math.to_decimal_number_with_round(x)
        result = self.base_math.to_decimal_number_with_round("0")
        #print("x", x)
        for i in range(int(iterations)):
            i = self.base_math.to_decimal_number_with_round(i)
            #print("i",i, type(i))
            one = self.base_math.to_decimal_number_with_round("-1")**i
            #print("one",one, type(one))
            two = x**(self.base_math.to_decimal_number_with_round("2")*i)
            #print("two",two, type(two))
            three = self.factorial(self.base_math.to_decimal_number_with_round("2")*i)
            #print("three", three, type(three))
            result += self.base_math.to_decimal_number_with_round(one*two/three)
        return result
    def tg(self, x):
        result = self.sin(x)/self.cos(x)
        return self.base_math.to_decimal_number_with_round(result)
    def ctg(self, x):
        result = self.cos(x)/self.sin(x)
        return self.base_math.to_decimal_number_with_round(result)
    

