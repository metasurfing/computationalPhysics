from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from fourier_transform import real_dft, real_idft
from numpy import arange, zeros, sin, sum
from math import pi
from pylab import plot, show, figure, xlim, ylim

N=1000
dx = 0.01
n = arange(0,N)
#square wave
n_start = 0
n_end = N/2-1
square = zeros(N,float)
for kk in range(N):
    if kk >= n_start and kk <= n_end:
        square[kk] = 1

#sawtooth
sawtooth = n

#modulated sine wave
mod_sine = sin(1*pi*n/N)*sin(20*pi*n/N)

#figure(1)
#plot(n,square)

figure(4)
plot(n,abs(real_dft(square)))
xlim(0,100)


#figure(2)
#plot(n,sawtooth)
# SAW_FT = real_dft(sawtooth)
# figure(5)
# plot(n,abs(SAW_FT))
# xlim(0,500)
# figure(9)
# plot(n,abs(real_idft(SAW_FT)))



#figure(3)
#plot(n,mod_sine)
figure(6)
plot(n,abs(real_dft(mod_sine)))
xlim(0,100)

show()
