# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

def g(x):
    if x <= -10 or x>7:
        print("ERROR: x is not in the range of (-10, 7]")
        exit()
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input the value for x: ")
x = float(x)

print("g(" + str(x) + ") = " + str(g(x)))
