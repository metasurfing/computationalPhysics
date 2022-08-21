from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from nlsolve import binary_search
from physical_constant import LightSpeed, Boltzmann, Planck
from numpy import exp

def func(x):
    return -5 + 5*exp(-x) + x

xsol = binary_search(func,1, 10)

print(xsol)
print(func(xsol))

c0 = LightSpeed()
h = Planck()
kB = Boltzmann()
l = 502e-9
b = h*c0/(kB*xsol)
T = b/l
print("The surface temperature of the Sun is: {} K".format(T))
