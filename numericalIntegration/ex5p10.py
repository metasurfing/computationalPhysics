import numInt as ni
from math import sqrt
import pylab as plt
from numpy import zeros, linspace

def V(x):
    return x**4

m = 1 #mass of particle
#a = 1 #height of particle
N = 20 #Number of sample points for Gaussian Quad
h = linspace(0.01,2,100)
T = zeros(len(h))

for kk in range(len(h)):
    a = h[kk]
    def f(x):
        return 1/sqrt(V(a) - V(x))

    s = ni.gaussQuadInt1D(f, 0, a, N)
    T[kk] = sqrt(8*m)*s

f1 = plt.figure(1)

plt.plot(h,T)
plt.xlabel('Height (m)')
plt.ylabel('Period (s)')
plt.show()
