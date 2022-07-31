from numInt import gaussQuadInt1D
from math import exp, pi, sqrt

def f(z):
    return exp(-(z**2)/(1-z)**2)/(1-z)**2

N = 50
a = 0.0
b = 1.0

I = gaussQuadInt1D(f,a,b,N)

print(I)
print(0.5*sqrt(pi))
