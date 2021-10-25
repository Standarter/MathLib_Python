from settings import Settings
from decimal import Decimal as number
class math_functions:
    sin = 0
    cos = 0
    tg = 0
    ctg = 0
    def OutputConvert(self, Number):
        Number = str(round(Number, int(Settings["FunctionsRoundTo"])))
        if Settings["NumberType"] == "Float":
            return float(Number)
        if Settings["NumberType"] == "Decimal":
            return number(Number)
    def __init__(self):
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
            self.sin = sin
            self.cos = cos
            self.tg = tg
            self.ctg = ctg
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
            self.sin = sin
            self.cos = cos
            self.tg = tg
            self.ctg = ctg