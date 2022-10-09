from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import loadtxt, fft, log10, abs, arange, zeros
from pylab import plot, show, ylabel, xlabel, title, figure

dow = loadtxt('./dow.txt')

dow_k = fft.rfft(dow)
Nd = len(dow_k)
Nnz = round(0.02*Nd)
dow_filter_k = zeros(Nd,complex)
dow_filter_k[0:Nnz] = dow_k[0:Nnz]
dow_smooth = fft.irfft(dow_filter_k)

plot(dow)
plot(dow_smooth)
show()
