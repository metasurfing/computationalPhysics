from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import array, sin, diag, zeros
from numpy.linalg import eigvalsh
from math import pi
from physical_constant import Planck_bar, LightSpeed
from linearAlg import eigH


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
Esh = eigvalsh(H)

print(H)
print(Esh/eV)
print(diag(E)/eV)
