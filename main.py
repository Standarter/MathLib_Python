from decimal import Decimal as number
import basic_functions
import math_functions
import analize_functions
import array_functions
import settings
import all_functions
import log

settings_initialize = settings.ProgramSettings().SettingsInit()
math_initialize = math_functions.math_functions()
array_initialize = array_functions.array_functions()

print(array_initialize.ArrayFunction([1,2,3,4,5], "x**number(1/2)"))
#a = 0.00
##print("SIN=",all_functions.sin(a))
#print("COS=",all_functions.cos(a))
#print("TG=",all_functions.tg(a))
#print("CTG=",all_functions.ctg(a))