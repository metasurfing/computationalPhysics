from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import array, sin, diag, zeros, linspace, sqrt
from numpy.linalg import eigvalsh
from math import pi
from physical_constant import Planck_bar, LightSpeed
from linearAlg import eigH
from numInt import gaussQuadInt1D
from pylab import plot, show


e_mass = 9.1094*10**-31
q_e = 1.6022*10**-19
eV = q_e
L = 5*10**-10
a = 10*eV
h_bar = Planck_bar()

M = 10
N = 10
H = zeros([M,N])
for mm in range(M):
    m = mm + 1
    odd_mm = m%2
    for nn in range(N):
        n = nn + 1
        odd_nn = n%2
        if mm == nn:
            H[mm,nn] = ((n*pi*h_bar/L)**2/e_mass + a)/2
        elif odd_mm != odd_nn:
            H[mm,nn] = -a*8/pi**2 *m*n/(m**2 - n**2)**2
        else:
            H[mm,nn] = 0



E, V = eigH(H,tol = 10**-6)
print(diag(E)/eV)

def phi(x,eigV,state,L,Nx,M):
    def wavefunction(xx):
        phi = 0
        for nn in range(M):
            phi = phi + eigV[nn,M-state]*sin((nn+1)*pi/L*xx)
        return phi
    def integrand(xx):
        return abs(wavefunction(xx))**2
    normalization = gaussQuadInt1D(integrand,0,L,100)
    phix = wavefunction(x)/sqrt(normalization)
    return phix

Nx = 101
x = linspace(0,L,Nx)

phi1 = phi(x,V,1,L,Nx,M)
phi2 = phi(x,V,2,L,Nx,M)
phi3 = phi(x,V,3,L,Nx,M)
plot(x,phi1)
plot(x,phi2)
plot(x,phi3)
show()
