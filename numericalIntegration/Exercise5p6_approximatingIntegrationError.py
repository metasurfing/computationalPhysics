#!/usr/bin/env python3

import numpy as np
from numInt import trapInt1D,simpInt1D

def f(x):
    return x**4 - 2*x + 1

N1 = 10
N2 = 20
a = 0.0
b = 2.0

It1 = trapInt1D(f,a,b,N1)
Is1 = simpInt1D(f,a,b,N1)

It2 = trapInt1D(f,a,b,N2)
Is2 = simpInt1D(f,a,b,N2)

print(It1)
print(Is1)

print('The approximate error using the trapezoidal rule is:')
print((abs(It2-It1)/3))
print('The true error using the trapezoidal rule is:')
print(It2-4.4)

print("The approximate error using Simpson's rule is:")
print(abs(Is2-Is1)/15)
print("The true error using Simpson's rule is:")
print(Is2-4.4)
