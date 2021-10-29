from basic_functions import *
import all_functions
import random
class math_basic:
    base_math = basic_functions()
    def __init__(self):
        all_functions.sin = self.sin
        all_functions.cos = self.cos
        all_functions.tg = self.tg
        all_functions.ctg = self.ctg
        all_functions.factorial = self.factorial
    def factorial(self, x):
        x = self.base_math.to_decimal_number(x)
        if x < -self.base_math.to_decimal_number("100"):
            result = self.base_math.to_decimal_number("1")
            x = self.base_math.to_decimal_number(x)
            #print(x)
            for i in range(1, int(x) + 1):
                result *= self.base_math.to_decimal_number(i)
                #print(result)
            return self.base_math.to_decimal_number_with_round(result)
        else:
            x = self.base_math.to_decimal_number(x)
            one = self.sqrt(2*all_functions.pi*x)
            two = (x/all_functions.e)**x
            three = 1
            for i in range(1, 25):
                one1 = self.bernully_numbers_2n(2*i)
                two1 = (2*i)*(2*i-1)*x**(2*i-1)
                three += one1/two1
            return one*two*three
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
    def arcsin(self, x):
        pass
    def arccos(self, x):
        return all_functions.pi/2 - self.arcsin(x)
    def binominal(self, n, k):
        n = self.base_math.to_decimal_number_with_round(n)
        k = self.base_math.to_decimal_number_with_round(k)
        one = self.factorial(n)
        two = self.factorial(k)*self.factorial(n-k)
        return self.base_math.to_decimal_number_with_round(one/two)
    def bernully_numbers_2n(self, n):
        import function_dataset.bernully as dataset
        if int(n) < len(dataset.bernully_dataset):
            return self.base_math.to_decimal_number_with_round(dataset.get_bernully(n))
        else:
            n = self.base_math.to_decimal_number_with_round(n)
            one = 2*(-1)**(n + 1)
            two = self.dzeta_function(2*n)*self.factorial(2*n)
            three = (2*all_functions.pi)**(2*n)
            return one*two/three
    def dzeta_function(self, x, roundto=5, fixed_iterations=None):
        import function_dataset.dzeta as dataset
        if int(x) < len(dataset.dzeta_dataset):
            return self.base_math.to_decimal_number_with_round(dataset.get_dzeta(x))
        else:
            x = self.base_math.to_decimal_number_with_round(x)
            nmin = self.base_math.to_decimal_number_with_round((1/10**-roundto))**(1/x)
            nmin = fixed_iterations if fixed_iterations != None else nmin
            #print("nmin", nmin)
            result = self.base_math.to_decimal_number_with_round("0")
            for i in range(1, int(nmin) + 1):
                result += 1/self.base_math.to_decimal_number_with_round(i)**x
            return self.base_math.to_decimal_number_with_round(result)
    def sqrt(self, x):
        x = self.base_math.to_decimal_number_with_round(x)
        #print(x)
        return all_functions.newton_method("x**2-{0}".format(x), random.randint(1, 10))
    

