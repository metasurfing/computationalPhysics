# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:11:01 2020

@author: ljszym
"""
from math import sqrt, pi
from numpy import arange, linspace

def f(x):
    return sqrt(1-x**2)

I = 0

L = 2
N = 100000

dx = L/N

for xx in linspace(-1,1-dx,N):
    I = I + f(xx+dx/2)*dx

print("The approximated integral is: ", I, "The exact integral is: ", pi/2)
print("Percent error in integral is: ", (I-pi/2)/(pi/2)*100)


#From the book
I=0
for kk in range(N):
    I = I + f(-1+dx*kk)*dx

print("The approximated integral is: ", I, "The exact integral is: ", pi/2)
print("Percent error in integral is: ", (I-pi/2)/(pi/2)*100)