from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4
from numpy import array, empty, linspace, sqrt
from pylab import plot, show, xlabel, ylabel, xlim, ylim, figure, legend

M = 10
G = 1
L = 2

def f(r,t):
    x = r[0]
    xdot = r[1]
    y = r[2]
    ydot = r[3]
    rad = sqrt(x**2 + y**2)
    fx1 = xdot
    fx2 = -x*G*M/rad**2/sqrt(rad**2 + L**2/4)
    fx3 = ydot
    fx4 = -y*G*M/rad**2/sqrt(rad**2 + L**2/4)
    return array([fx1, fx2, fx3, fx4],float)

t = linspace(0,10,1000)
t0 = 0
x0 = [1,0,0,1]
x_sol = rk4(f,t,x0,t0)

plot(x_sol[2,:], x_sol[0,:])
show()
