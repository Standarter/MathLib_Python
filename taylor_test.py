from basic_functions import basic_functions
from math_analisys import math_analisys
from numbers_methods import numbers_methods
from math_basic import *
import all_functions
bf = basic_functions()
mb = math_basic()
ma = math_analisys()
na = numbers_methods()
from basic_functions import *
def for_sin(x_max, p):
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while abs(x_max**(2*i+1)/mb.factorial(2*i+1)) > dx:
        i += 1
    print("For (sin) n equals:", i, "with p equals", p)
def for_arcsin(x_max, p):
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while abs((mb.factorial(2*i)*x_max**(2*i+1))/(4**i*(mb.factorial(i)**2)*(2*i+1))) > dx:
        i += 1
    print("For (arcsin) n equals:", i, "with p equals", p)
def for_cos(x_max, p):
    mb = math_basic.math_basic()
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while abs(x_max**(2*i)/mb.factorial(2*i)) > dx:
        i += 1
    print("For (cos) n equals:", i, "with p equals", p)
def for_arccos(x_max, p):
    mb = math_basic.math_basic()
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while abs((mb.factorial(2*i)*x_max**(2*i+1))/(4**i*(mb.factorial(i)**2)*(2*i+1))) > dx:
        i += 1
    print("For (arccos) n equals:", i, "with p equals", p)
bf = basic_functions()
#p = int(input("Enter number symbols after dot: "))
#for_sin(2*all_functions.pi, p)
#for_cos(2*all_functions.pi, p)
for i in range(1, 10):
    for_arcsin(1, i)
#for_arccos(1, p)