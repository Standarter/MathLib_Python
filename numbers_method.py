import basic_functions
import analize_functions
import all_functions
from settings import Settings, RoundTo
from decimal import Decimal as number
import log

class numbers_method:
    analize = analize_functions.analize_functions()
    base_math = basic_functions.basic_functions()
    def number_inequationsX(self):
        pass
    def solve_inequationsX(self):
        pass
    def arcsin_newtonX(self, x, x0=all_functions.pi, iterations=10):
        x = self.base_math.OutputConvert(x)
        x0 = self.base_math.OutputConvert(x0)
        result = self.newton_methodX("sin(x)-{0}".format(x), x0, iterations=iterations)
        return self.base_math.OutputConvert(result)
    def arccos_newtonX(self, x, x0=all_functions.pi, iterations=10):
        x = self.base_math.OutputConvert(x)
        x0 = self.base_math.OutputConvert(x0)
        result = self.newton_methodX("cos(x)-{0}".format(x), x0, iterations=iterations)
        return self.base_math.OutputConvert(result)
    def newton_methodX(self, function, x0, iterations=15, SolveAccuracy = RoundTo):
        x1 = x0 + x0**(x0+1)
        while abs(x0 - x1) > 0:
            x1 = x0
            fx = self.base_math.solve_function(function, variables={"x": x0})
            dfx = self.analize.DerivedX(function, x0)
            try:
                x0 = x0 - fx/dfx
                iterations -= 1
                #log.error("x0", self.base_math.OutputConvert(x0))
            except:
                return self.base_math.OutputConvert(x0)
        return self.base_math.OutputConvert(x0)
        