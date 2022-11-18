from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from linearAlg import gaussElim
from numpy import zeros, exp, arange, real
from physical_constant import Planck_bar, electron_mass
from pylab import plot, show
from vpython import curve, rate, vector

hbar = Planck_bar()
me = electron_mass()
L = 1e-8
x0 = L/2
sigma = 1e-10
kappa = 5e10
N = 1000
Nt = 10000
a = L/N
h = 1e-18

#Initialize the wavefunction
xgrid = arange(0,L,a)
psi = zeros([N,Nt],complex)
psi[:,0] = exp(-(xgrid - x0)**2/(2*sigma**2))*exp(1j*kappa*xgrid)


#Calculate values of tridiagonal matrices
a1 = 1 + h * 1j*hbar/(2*me*a**2)
a2 = -h*1j*hbar/(4*me*a**2)

b1 = 1 - h * 1j*hbar/(2*me*a**2)
b2 = h * 1j*hbar/(4*me*a**2)

#Initial A matrix
A = zeros([N-2,N-2],complex)
for ii in range(0,N-2):
    for jj in range(0,N-2):
        if ii == jj:
            A[ii,jj] = a1
        elif abs(ii-jj) == 1:
            A[ii,jj] = a2

scale = 1e-9
string = curve(vector(xgrid[0],scale*real(psi[0,0]),0),vector(xgrid[1],scale*real(psi[1,0]),0))
for ii in range(2,N):
    string.append(vector(xgrid[ii],scale*real(psi[ii,0]),0))

for kk in range(1,Nt):

    #Create source vector
    v = b1*psi[1:N-1,kk-1] + b2*(psi[2:N,kk-1] + psi[0:N-2,kk-1])

    #Solve for solution at next time step
    psi[1:N-1,kk] = gaussElim(A,v,opts = 'banded',above=1, below=1)

    rate(500)
    for ii in range(0,N):
        # string.modify(ii,y=scale*Phi[ii])
        string.modify(ii,y=scale*real(psi[ii,kk]))

#Description:
# The wavefunction is initially localized to a gaussian with a phase progression across it.
# However it spreads out and reflects off of the boundaries until it forms a standing wave
# interference pattern.
# The phase progression means the pulse (gaussian) is propagating along the axis; however, since the gaussian
# envelope is not a solution to the wave equation the envelope disperses as it propagates due to the different
# wavenumbers that compose the gaussian. The hard boundary condition causes it to reflect off the
# boundaries until the wave is fully dispersed and the different wavenumbers composing the gaussian set up
# the standing wave interference pattern.
