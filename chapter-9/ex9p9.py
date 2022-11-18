from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/resources/')
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from dcst import dst, idst
from numpy import zeros, exp, arange, real, imag, cos, sin, pi
from physical_constant import Planck_bar, electron_mass
from pylab import plot, show
from vpython import curve, rate, vector

hbar = Planck_bar()
me = electron_mass()
L = 1e-8
x0 = L/2
t0 = 0
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

#Real and imaginary parts of the initial wave function
psi0r = real(psi[:,0])
psi0i = imag(psi[:,0])

#create array with indices for coefficients
k = arange(0,N,1)

#Discrete sine transforms
ak = dst(psi0r)
nk = dst(psi0i)
Ek = pi**2*hbar**2/(2*me*L**2)*k**2

scale = 1e-9
string = curve(vector(xgrid[0],scale*real(psi[0,0]),0),vector(xgrid[1],scale*real(psi[1,0]),0))
for ii in range(2,N):
    string.append(vector(xgrid[ii],scale*real(psi[ii,0]),0))

for tt in range(1,Nt):

    t = t0 + tt*h
    #Solve for solution at next time step
    psi[:,tt] = idst(ak*cos(Ek/hbar*t) - nk*sin(Ek/hbar*t))

    rate(500)
    for ii in range(0,N):
        # string.modify(ii,y=scale*Phi[ii])
        string.modify(ii,y=scale*real(psi[ii,tt]))

#Description:
#The wave function propagates in the opposite direction from the previous solution.
#This is governed by the time evolution exp(iE/hbar*t) being positive delay (backward propagation)
#Otherwise the answer is similar to the previous problem:
# The wavefunction is initially localized to a gaussian with a phase progression across it.
# However it spreads out and reflects off of the boundaries until it forms a standing wave
# interference pattern.
# The phase progression means the pulse (gaussian) is propagating along the axis; however, since the gaussian
# envelope is not a solution to the wave equation the envelope disperses as it propagates due to the different
# wavenumbers that compose the gaussian. The hard boundary condition causes it to reflect off the
# boundaries until the wave is fully dispersed and the different wavenumbers composing the gaussian set up
# the standing wave interference pattern.
