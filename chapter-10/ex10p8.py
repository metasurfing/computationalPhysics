from numpy.random import rand
from numpy import sum, exp, sqrt

Npts = 1000000

xs = rand(Npts)**2

I = 2/Npts*sum(1/(exp(xs)+1))
print(I)
