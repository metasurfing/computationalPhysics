import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from numpy import exp, arange, zeros
from math import pi, factorial

def f(z):
    return exp(2*z)

N = 10000
k = arange(10000)

M = 20
Df =  zeros(20)
zk = exp(2j*pi*k/N)

for mm in range(M):
    Df[mm] = factorial(mm+1)/N*sum(f(zk)*exp(-2j*pi*(mm+1)*k/N))

print(Df)
