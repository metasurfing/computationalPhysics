# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:02:49 2021

@author: ljszym
"""


def f(x):
    return x**4 - 2*x + 1

a = 0
b = 2
N = 1000

h = (b-a)/N

s = (f(a)+f(b))

for kk in range(1,N,2):
    s += 4*f(a+kk*h)

for kk in range(2,N-1,2):
    s += 2*f(a+kk*h)
    
I = s*h/3

print(I)

fractional_error = (I-4.4)/4.4
print("The fractional error is: ",fractional_error)

"""
The fractional error with N=100
Trap: ~2.42x10^-4
Simp: ~9.7x10^-9

The fractional error with N=1000
Trap: ~2.42x10^-6
Simp: ~9.7x10^-13
"""