# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:24:11 2021

@author: ljszym
"""
from math import exp
from numpy import empty, arange
from pylab import plot, show

def f(x):
    return exp(-x**2)

x1 = 0
x2 = 3
dx = 0.1
N = 1000
x = list(arange(x1,x2+dx,dx))

Ex = empty([len(x),1],float)

for nn in range(0,31):
    a = x1
    b = nn*dx
    h = (b-a)/N
    s = f(a)+f(b)
    
    for kk in range(1,N,2):
        s += 4*f(a+kk*h)
    
    for kk in range(2,N-1,2):
        s += 2*f(a+kk*h)
        
    Ex[nn,0] = s*h/3
   
plot(x,Ex)
show()