from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from nlsolve import golden_search
from numpy import exp, linspace
from pylab import plot, show, ylim

V0 = 1
sigma = 1 #in nanometers
tol = 1e-6 #in nanometers

def V(r):
    return V0*((sigma/r)**6 - exp(-r/sigma))

rplot = linspace(1,8,101)

r1 = 1
r4 = 4

rmin = golden_search(V, r1, r4)
print(rmin)
plot(rplot,V(rplot))
plot(rmin, V(rmin),'ko')
ylim(-0.5, 0.5)
show()
