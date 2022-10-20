from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from ode import leapfrog
from numpy import array
from pylab import plot, show, xlabel, ylabel

def f(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = y**2 - x - 5
    return array([fx, fy], float)

t = [0, 50]
h = 0.001
x0 = [1, 0]

[x_sol, t_sol] = leapfrog(f,t,x0,h)


plot(t_sol,x_sol[0,:])
show()
