from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from ode import rk4

from numpy import empty, array, linspace
from pylab import plot, legend, show, xlabel, ylabel, figure

s = 10
rho = 28
b = 8/3


def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]

    fx = s*(y-x)
    fy = rho*x-y-x*z
    fz = x*y - b*z

    return array([fx, fy, fz], float)

t0 = 0
tf = 50
x0 = array([0, 1, 0], float)
t = linspace(0,tf, 5000)

xsol = rk4(f,t,x0,t0)

figure(1)
plot(t,xsol[1,:])
xlabel('Time')
ylabel("y(t)")

figure(2)
plot(xsol[0,:],xsol[2,:])
xlabel('x(t)')
ylabel('z(t)')
show()
