from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import zeros, log10, array, sin, pi, arange, floor, fft, matlib
from fourier_transform import fastFT

from pylab import plot, show, figure, imshow, gray

def q(u,alpha):
    return abs(sin(u*alpha))


d = 20e-6
alph = pi/d
w = 200e-6
W = 2e-3
lam = 500e-9
f = 1
L = 10e-2
N = int(floor(W/(lam*f)*L)+1)

xk = arange(0,N)*lam*f/W - L/2
un = arange(0,N)*W/N - W/2

grating_fnc = zeros(N,float)
for nn in range(0,N):
    if un[nn] >= -w/2 and un[nn] <= w/2:
        grating_fnc[nn] = q(un[nn],alph)

I_xk = fft.fft(grating_fnc)
Intensity = (W/N)**2*abs(fft.fftshift(I_xk))**2
Nk = int(N/4)
plotIntensity = matlib.repmat(Intensity,Nk,1)

figure(1)
plot(un, grating_fnc)

figure(2)
plot(xk,Intensity)

figure(3)
imshow(plotIntensity)
show()
