#The relaxation equation is:
# x(t) = 1/2 * [ x(t+h) + x(t-h) + g*h^2 ]
from numpy import zeros, arange, empty, amax
from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from physical_constant import standard_gravity
from pylab import plot, show

g = standard_gravity()
N = 100
t0 = 0
x0 = 0
tf = 10
xf = 0
h = (tf-t0)/N

#Grid of time steps for the solution
tgrid = arange(t0,tf,h)

#array to hold solutions for x
x = zeros(N,float)
xp = empty(N,float)
x[0] = x0
x[N-1] = xf
xp[0] = x0
xp[N-1] = xf

delta = 1e-6
epsilon = 2*delta

while epsilon >= delta:
    xp[1:N-1] = 0.5 * ( x[2:N] + x[0:N-2] + g*h**2 )
    x, xp = xp, x
    epsilon = amax(abs(xp-x))

plot(tgrid,x)
show()

print('The approximate initial velocity is:', (x[1]-x[0])/h, 'm/s')
