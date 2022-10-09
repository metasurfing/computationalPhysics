from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from numpy import cos, linspace, imag
from fourier_transform import real_dft, real_idft
from math import pi
from pylab import plot, show, figure
N = 101
xn = linspace(0,10,N)
n = linspace(0,N-1,N)
f = cos(2*pi/10*xn) + cos(2*pi/5*xn)

c = real_dft(f)
y_idft = real_idft(c)

fig1 = figure(1)
plot(xn,f)
plot(xn,y_idft,'ko')

fig2 = figure(2)
plot(n/10,abs(c),'ko')
show()
