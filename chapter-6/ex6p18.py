from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import exp, linspace, empty
from physical_constant import Planck, LightSpeed, Boltzmann
from numInt import gaussQuadInt1D, gaussxw
from math import pi
from pylab import plot, show
from nlsolve import golden_search

Ns = 100
h = Planck()
c = LightSpeed()
kB = Boltzmann()
l1 = 390*1e-9
l2 = 750*1e-9
Nt = 101
T = linspace(300,10000, Nt)

x, w = gaussxw(Ns)



nk = empty(Nt,float)

def integrand(x):
    return x**3/(exp(x)-1)

def efficiency(Temp):
    ak = h*c/l2/kB/Temp
    bk = h*c/l1/kB/Temp
    xcur, wcur = 0.5*(bk-ak)*x + 0.5*(ak+bk), 0.5*(bk-ak)*w
    return 15/pi**4*gaussQuadInt1D(integrand,xk = xcur, wk = wcur, N = Ns)

for tt in range(Nt):
    nk[tt] = efficiency(T[tt])

T1 = 6000
T4 = 8000
def fmin(Temp):
    return -efficiency(Temp)

Tmax = golden_search(fmin, T1, T4, tol = 1)

plot(T,nk)
plot(Tmax,efficiency(Tmax),'ko')
print(Tmax)
show()

#The max efficiency temp is ~6928 K which is not practical since Tungsten melts at 3695 K.
