from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from pylab import plot, show
from nlsolve import secant_method, newton_method
from numpy import linspace

w = 2.662*1e-6
G = 6.674*1e-11
M = 5.974*1e24
m = 7.348*1e22
R = 3.844*1e8
def g(r):
    return r*w**2 - ((G*M)/r**2 - (G*m)/(r-R)**2)

r0 = 1e8

rplot = linspace(0.2e8, 3.8e8, 1001)
plot(rplot, g(rplot))

rsol = secant_method(g,r0,tol = R/2*1e-10, maxIter = 100)
print("The distance is: {} km".format(rsol/1e3))
print(g(rsol))

plot(rsol,g(rsol),'ro')
# plot(r0,g(r0),'ko')
show()
