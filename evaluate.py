#Given a variable named a and another variable named b, create a Python program (Filename: evaluate.py) to evaluate the following equations:


import numpy as np
import math


# print(math.exp(1)) # e^1 ==> 2.718...
# print(np.exp(1))   # e^1 ==> 2.718...
# print(3**4)        # 3^4 ==> 81
# print(np.square(4))  # 4^2 ==> 16


def Y1(a, b):
    return np.square(a+b)


def Y2(a, b):
    return np.square(a)+np.square(b)+2*a*b


def Y3(a, b):
    return np.sin(a) + b**4 + np.exp(2*a+b)


def Y4(a, b):
    return np.cos(a) + 2**b + np.exp(a-b)


print(Y1(4,8))
print(Y2(4,8))
print(Y3(4,8))
print(Y4(4,8))