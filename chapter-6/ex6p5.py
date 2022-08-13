from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from numpy import array, cdouble
from numpy.linalg import solve
from linearAlg import gaussElim
from cmath import polar, phase
from math import pi

Vp = 3
R1 = 1000
R3 = 1000
R5 = 1000
R2 = 2000
R4 = 2000
R6 = 2000
C1 = 1*10**-6
C2 = 0.5*10**-6
omega = 1000

A = array([[1/R1+1/R4+1j*omega*C1, -1j*omega*C1, 0],
          [-1j*omega*C1, 1/R2+1/R5+1j*omega*(C1+C2), -1j*omega*C2],
          [0,-1j*omega*C2, 1/R3+1/R6+1j*omega*C2]],dtype=complex)
v = array([Vp/R1, Vp/R2, Vp/R3],dtype=complex)

# x, L, U, swaps = gaussElim(A,v,opts='LU')
x = solve(A,v)


for kk in range(len(x)):
    r, phi = polar(x[kk])
    print('Voltage',kk)
    print('Amplitude:',r)
    print('Phase:',phi*180/pi)
