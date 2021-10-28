from decimal import Decimal as number
import basic_functions
import math_functions
import analize_functions
import array_functions
import numbers_method
import settings
import all_functions
import log
import math

settings_initialize = settings.ProgramSettings()
math_initialize = math_functions.math_functions()
analize_initialize = analize_functions.analize_functions()
array_initialize = array_functions.array_functions()
numbers_method_initialize = numbers_method.numbers_method()

#print(analize_initialize.DifferencialX("x**2", 2))
#print(analize_initialize.DerivedX("x**2", 2))
temp = numbers_method_initialize.newton_methodX("sin(x)-number(1)", 1, iterations=100)
print(temp)
print(math.degrees(temp))
print(all_functions.sin(temp))
#print(all_functions.sin(all_functions.pi/2))