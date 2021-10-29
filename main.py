from basic_functions import basic_functions
from math_basic import math_basic
from math_analisys import math_analisys
from numbers_methods import numbers_methods
import all_functions
bf = basic_functions()
mb = math_basic()
ma = math_analisys()
na = numbers_methods()

start = False
#print(mb.dzeta_function(3))
#print(mb.bernully_numbers_2n(1))
print(mb.factorial(5))
#print(mb.sin(all_functions.pi/2, 26))
#print(mb.cos(all_functions.pi/2, 26))
#for i in range(0, 10 + 1):
#    print(i,mb.bernully_numbers(i))
#if start == True:
#    while True:
#        test = input("Enter command: ")
#        temp1 = bf.default_function(test, variables={"x": 0.1})
#        print(temp1)