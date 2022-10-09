from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from numpy import ones, empty, fft, zeros
from pylab import plot, show

square = ones(1000, float)
square[0:499] = -square[0:499]

s_k = fft.rfft(square)
Nk = len(s_k)
Nnz = 9
s_k_filter = zeros(Nk, complex)
s_k_filter[0:Nnz] = s_k[0:Nnz]
square_smooth = fft.irfft(s_k_filter)

plot(square)
plot(square_smooth)
show()

#The wiggles are a result of the discontinuity in the square wave.
#These discountinuities require infinite bandwidth and result in wiggles and overshoot
#when using bandlimited representations.
