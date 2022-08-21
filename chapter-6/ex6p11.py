from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from nlsolve import relaxationNd, overrelaxationNd
from numpy import exp, empty, arange
from pylab import plot, show, xlabel, ylabel

c = 2

def func(x):
    return 1-exp(-c*x)

Nvars = 1
x0 = empty(Nvars,float)
for kk in range(Nvars):
    x0[kk] = 1

xsol, iter = relaxationNd(func,x0,tol = 1e-6, count = 1)
xsolo, itero = overrelaxationNd(func,x0,tol = 1e-6, count = 1, w = 0.7)
print(xsol)
print(iter)

print(xsolo)
print(itero)

#Part d:
#I think it could be useful for functions where f(x)<0 when x>x* and f(x)>0 when x<x*
#In this scenario reducing the step size slightly would bring consecutive steps closer to the
#fixed point of the function faster.
