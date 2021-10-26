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
a = 0.00
print("SIN=",all_functions.sin(a))
print("COS=",all_functions.cos(a))
print("TG=",all_functions.tg(a))
print("CTG=",all_functions.ctg(a))