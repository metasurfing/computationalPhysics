from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from fourier_transform import dct, idct
from numpy import loadtxt, floor, zeros
from pylab import plot, show, figure
from numpy import fft

dow = loadtxt('./dow.txt')
dow2 = loadtxt('./dow2.txt')

dow2k = fft.rfft(dow2)
N2k = len(dow2k)
N2kf = int(N2k*0.02)
dow2k_filter = zeros(N2k,complex)
dow2k_filter[0:N2kf] = dow2k[0:N2kf]
dow2k_smooth = fft.irfft(dow2k_filter)

dow2kc = dct(dow2)
N2kc = len(dow2kc)
N2kfc = int(N2kc*0.02)
dow2kc_filter = zeros(N2kc,complex)
dow2kc_filter[0:N2kfc] = dow2kc[0:N2kfc]
dow2kc_smooth = idct(dow2kc_filter)

figure(1)
plot(dow2)
plot(dow2k_smooth)
plot(dow2kc_smooth)
show()
