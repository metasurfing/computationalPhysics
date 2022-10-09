from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import fft, loadtxt, empty, log10, array
from fourier_transform import fastFT

from pylab import plot, show

pitch = loadtxt('./pitch.txt')

# pitch = array([1, 0.5, 0,-0.5, -1, -0.5, 0, 0.5])
# pitch = array([1, 0.5, 0,-0.5])
ak = fft.fft(pitch)
ak_my = empty(len(pitch),complex)
ak_my = fastFT(pitch)

plot(abs(ak))
plot(abs(ak_my))
show()
