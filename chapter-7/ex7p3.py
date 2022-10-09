from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import loadtxt, fft, log10, abs, arange
from pylab import plot, show, ylabel, xlabel, title, figure

piano = loadtxt('./piano.txt')
trumpet = loadtxt('./trumpet.txt')
piano_a = fft.rfft(piano)
trumpet_a = fft.rfft(trumpet)

Nt = len(trumpet)
Np = len(piano)
Fs = 44100

#Using this frequency conversion the instruments are playing C5
fp = arange(0,Np)/Np*Fs
ft = arange(0,Nt)/Nt*Fs

figure(1)
plot(fp[1:10000],abs(piano_a[1:10000]))
plot(ft[1:10000],abs(trumpet_a[1:10000]))
title('Spectrum')
ylabel('Fourier coefficients')
xlabel('Frequency (Hz)')
show()

# figure(1)
# plot(fp[1:10000],20*log10(abs(piano_a[1:10000])))
# title('Spectrum of piano note')
# ylabel('Fourier coefficients (dB)')
# xlabel('Normalized Frequency')

# figure(2)
# plot(ft[1:10000],20*log10(abs(trumpet_a[1:10000])))
# title('Spectrum of trumpet note')
# ylabel('Fourier coefficients (dB)')
# xlabel('Normalized Frequency')
# show()
