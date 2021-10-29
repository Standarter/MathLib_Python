from basic_functions import basic_functions
from math_basic import math_basic
from math_analisys import math_analisys
import all_functions
bf = basic_functions()
mb = math_basic()
ma = math_analisys()

start = False

print(mb.sin(all_functions.pi/2, 26))
print(mb.cos(all_functions.pi/2, 26))

#if start == True:
#    while True:
#        test = input("Enter command: ")
#        temp1 = bf.default_function(test, variables={"x": 0.1})
#        print(temp1)