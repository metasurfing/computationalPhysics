from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from fourier_transform import real_dft
from numpy import arange, zeros, sin, sum, loadtxt, abs
from math import pi
from pylab import plot, show, figure, xlim, ylim

sunspots = loadtxt('sunspots.txt')
ck = real_dft(sunspots[:,1])

figure(1)
plot(sunspots[:,0],sunspots[:,1])
# Approximately 130 month period

figure(2)
plot(sunspots[1:30,0],abs(ck[1:30])**2)
show()

#Peak at k = 24
Ns = len(ck)
T = Ns/24

print(T)
#Period is 130.96 months. Close to approximated value
