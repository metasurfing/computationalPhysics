#!/usr/bin/env python3

from numInt import trapInt1D, simpInt1D
from math import sin, sqrt

def f(x):
  return (sin(sqrt(100*x)))**2

simpInt1D(f,a=0,b=1,N=2,opt = 'adaptive', AbsTol = 10**-6, pout = 1)
trapInt1D(f,a=0,b=1,N=2,opt = 'Romberg', AbsTol = 10**-6, pout = 1)
