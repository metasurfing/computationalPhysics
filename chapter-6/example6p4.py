from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from nlsolve import newton_method
from numpy import tanh, cosh, arange, empty
from pylab import plot, show

u = arange(-0.99, 0.99, 0.01)

xsol = empty(len(u),float)
def gradient(x):
    return 1/cosh(x)**2

for kk in range(len(u)):
    def func(x):
        return tanh(x) - u[kk]

    xsol[kk] = newton_method(func,0,tol = 1e-12, grad = gradient, maxIter = 10)

plot(u,xsol)
show()
