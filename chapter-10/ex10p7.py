from numpy.random import rand
from numpy import sum

Npoints = 1000000
Ndim = 10
# Ndim = 2 #Check that the area is pi

samples = 2*rand(Npoints,Ndim) - 1

f = sum(samples**2,axis=1)

I = 2**Ndim/Npoints*sum(f<=1)

print(I)
