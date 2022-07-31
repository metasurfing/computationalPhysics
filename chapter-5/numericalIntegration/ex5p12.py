from numInt import gaussQuadInt1D, trapInt1D
from math import exp, pi
from physical_constant import Boltzmann, Planck_bar, LightSpeed

kB = Boltzmann()
h_bar = Planck_bar()
c0 = LightSpeed()

def w(z):
    return (z)**3/((exp(z/(1-z))-1)*(1-z)**5)

a = 0.00
b = 0.999
N = 50

s = gaussQuadInt1D(w,a,b,N)

sigma = kB**4/(h_bar**3*(2*pi*c0)**2)*s

print(sigma)
