from decimal import Decimal as number
from settings import Settings
import all_functions
import log
import basic_functions
import all_functions
class array_functions:
    bf = basic_functions.basic_functions()
    def __init__(self):
        all_functions.arrayAVG = self.ArrayAVG
        log.log("loaded", "arrayAVG", level=3)
        all_functions.arrayMIN = self.ArrayMIN
        log.log("loaded", "arrayMIN", level=3)
        all_functions.arrayMAX = self.ArrayMAX
        log.log("loaded", "arrayMAX", level=3)
        all_functions.arrayFUNC = self.ArrayFunction
        log.log("loaded", "arrayFUNC", level=3)
    def ArrayFunction(self, array, formula):
        for i in range(len(array)):
            array[i] = self.bf.solve_function(formula, {"x": array[i]})
        return array
    def ArrayAVG(self, array):
        result = 0
        for element in array:
            result += element
        return result/len(array)
    def ArrayMIN(self, array):
        result = array[0]
        for element in array:
            if element < result:
                result = element
        return result
    def ArrayMAX(self, array):
        result = array[0]
        for element in array:
            if element > result:
                result = element
        return result