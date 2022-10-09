from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from fourier_transform import real_dft
from numpy import loadtxt
from pylab import plot, xlim, show

y = loadtxt("pitch.txt", float)
c = real_dft(y)

plot(abs(c))
xlim(0,500)
show()
