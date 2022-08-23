from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from nlsolve import golden_search
from numpy import exp, linspace, empty, array
from pylab import plot, show, ylim

V0 = 1
sigma = 1 #in nanometers
tol = 1e-6 #in nanometers

def V(r):
    Vo = empty(len(r),float)
    Vo[abs(r)>1e-10] = V0*((sigma/r[abs(r)>1e-10])**6 - exp(-r[abs(r)>1e-10]/sigma))
    Vo[abs(r)<1e-10] = V0*1e20
    return Vo


rplot = linspace(1,8,101)

r1 = array([1.0])
r4 = array([1.5])

rmin = golden_search(V, r1, r4)
print(rmin)
plot(rplot,V(rplot))
plot(rmin, V(rmin),'ko')
ylim(-0.5, 0.5)
show()
