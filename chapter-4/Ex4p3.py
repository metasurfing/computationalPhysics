# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:47:31 2020

@author: ljszym
"""
from pylab import plot, show
from numpy import array, empty

def f(x):
    return x*(x-1)

delta = 10**-2
x0 = 1
Df = (f(x0+delta)-f(x0))/delta

print("The derivative at x = ", x0, "is Df = ", Df)

delta = [10**-4,10**-6,10**-8,10**-10,10**-12]
Df_d = empty([len(delta),1], float)

for d in range(len(delta)):
    Df_d[d] = (f(x0+delta[d])-f(x0))/delta[d]

plot(list(range(len(delta))), Df_d)
show()    