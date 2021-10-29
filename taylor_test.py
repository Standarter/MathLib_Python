import math_basic
from basic_functions import *
def for_sin(x_max, p):
    mb = math_basic.math_basic()
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while x_max**(2*i+1)/mb.factorial(2*i+1) > dx:
        i += 1
    print("For (sin) n equals:", i, "with p equals", p)
def for_cos(x_max, p):
    mb = math_basic.math_basic()
    dx = Decimal("1")/Decimal("10")**p
    i = 1
    while x_max**(2*i)/mb.factorial(2*i) > dx:
        i += 1
    print("For (cos) n equals:", i, "with p equals", p)
bf = basic_functions()
p = int(input("Enter number symbols after dot: "))
for_sin(2*all_functions.pi, p)
for_cos(2*all_functions.pi, p)