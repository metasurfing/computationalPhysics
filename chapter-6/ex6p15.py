from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from nlsolve import newton_method
from numpy import linspace, array, empty
from pylab import plot, show

def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
def dP(x):
    return 6*924*x**5 - 5*2772*x**4 + 4*3150*x**3 - 3*1680*x**2 + 840*x - 42

xx = linspace(0,1,101)

plot(xx,P(xx))


x0 = array([0.05, 0.2, 0.4, 0.6, 0.8, 0.9])
xzeros = empty(len(x0),float)
for kk in range(len(x0)):
    xzeros[kk] = newton_method(P,x0[kk],tol=1e-12,grad = dP)

plot(xzeros,P(xzeros),'ko')
show()
