from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import array, arange, sqrt
from physical_constant import electron_charge, Planck_bar, electron_mass
from nlsolve import secant_method, binary_search
from pylab import plot, show
from numInt import trapInt1D

e = -electron_charge()
m = electron_mass()
hbar = Planck_bar()
a = 1e-11
V0 = 50*e
x1 = -10*a
x2 = 10*a
N = 1000
h = (x2-x1)/N

# Harmonic oscillator
# def V(x):
#     return V0*(x/a)**2
#E0 = 138.020 eV
#E1 = 414.060 eV
#E2 = 690.101 eV

# Anharmonic oscillator
def V(x):
    return V0*(x/a)**4

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = 2*m/hbar**2*(V(x)-E)*psi
    return array([fpsi,fphi],float)

def solve(E):
    psi = 0.0
    phi = 1.0

    r = array([psi, phi],float)

    for xx in arange(x1,x2,h):
        k1 = h*f(r,xx,E)
        k2 = h*f(r+0.5*k1,xx+0.5*h,E)
        k3 = h*f(r+0.5*k2,xx+0.5*h,E)
        k4 = h*f(r+k3,xx+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]

def Psi(E,xi,xf,hx):
    psi = 0.0
    phi = 1.0
    psi_x = []

    r = array([psi, phi],float)

    for xx in arange(xi,xf,hx):
        k1 = hx*f(r,xx,E)
        k2 = hx*f(r+0.5*k1,xx+0.5*hx,E)
        k3 = hx*f(r+0.5*k2,xx+0.5*hx,E)
        k4 = hx*f(r+k3,xx+hx,E)
        r += (k1+2*k2+2*k3+k4)/6
        psi_x.append(r[0])


    return psi_x
#Harmonic oscillator solution
# Esol0 = secant_method(solve,e,tol=e*1e-3)
# Esol1 = secant_method(solve,1.7*Esol0,tol=e*1e-3,maxIter=50)
# Esol2 = secant_method(solve,3*Esol0,tol=e*1e-3)

# Anharmonic oscillator
#Secant method hits stationary points and causes false convergence
# Esol0 = secant_method(solve,e,tol=e*1e-6)
# Esol1 = secant_method(solve,1.6*Esol0,tol=e*1e-6,maxIter=50)
# Esol2 = secant_method(solve,1.62*Esol0,tol=e*1e-6)
#Binary search avoids convergence issues
Esol0 = binary_search(solve,0,300*e,tol=e*1e-6)
Esol1 = binary_search(solve,Esol0+50*e,Esol0+600*e,tol=e*1e-6)
Esol2 = binary_search(solve,1000*e,1500*e,tol=e*1e-6)
print('The ground state is:',Esol0/e,'eV')
print('The first excited state is:',Esol1/e,'eV')
print('The second excited state is:',Esol2/e,'eV')
print('The first spacing is:', Esol1/e-Esol0/e)
print('The second spacing is:', Esol2/e-Esol1/e)
xi = -5*a
xf = 5*a
hx = (xf-xi)/N
psi0 = Psi(Esol0,xi,xf,hx)
psi1 = Psi(Esol1,xi,xf,hx)
psi2 = Psi(Esol2,xi,xf,hx)

#Note: large values at the end appear to come from small errors in the value of E (the eigenvalues)
#These errors mean that the function does not quite satisfy the boundary conditions, resulting
#in spurious values at the end of the wave function.
#integrate using Simpson's rule
se0 = 0.0
so0 = 0.0
s0 = abs(psi0[0])**2 + abs(psi0[-1])**2

se1 = 0.0
so1 = 0.0
s1 = abs(psi1[0])**2 + abs(psi1[-1])**2

se2 = 0.0
so2 = 0.0
s2 = abs(psi2[0])**2 + abs(psi2[-1])**2

for ii in range(2,N-2,2):
    se0 += abs(psi0[ii])**2
    se1 += abs(psi1[ii])**2
    se2 += abs(psi2[ii])**2

for kk in range(1,N-1,2):
    so0 += abs(psi0[ii])**2
    so1 += abs(psi1[ii])**2
    so2 += abs(psi2[ii])**2

Ipsi0 = hx/3*(s0 + 2*se0 + 4*so0)
Ipsi1 = hx/3*(s1 + 2*se1 + 4*so1)
Ipsi2 = hx/3*(s2 + 2*se2 + 4*so2)
psi0n = psi0/sqrt(Ipsi0)
psi1n = psi1/sqrt(Ipsi1)
psi2n = psi2/sqrt(Ipsi2)

plot(arange(xi,xf,hx)/a,psi0n)
plot(arange(xi,xf,hx)/a,psi1n)
plot(arange(xi,xf,hx)/a,psi2n)
show()

#Integrate the normalized wave function
# se0 = 0.0
# so0 = 0.0
# s0 = abs(psi0n[0])**2 + abs(psi0n[-1])**2
#
# for ii in range(2,N-2,2):
#     se0 += abs(psi0n[ii])**2
#
# for kk in range(1,N-1,2):
#     so0 += abs(psi0n[ii])**2
#
# Ipsi0n = hx/3*(s0 + 2*se0 + 4*so0)
# print(Ipsi0n)
#Look at solve(E)
# Erange = arange(0,350*e,e)
# s = []
# for ee in Erange:
#     s.append(solve(ee))
#
# plot(Erange/e,s)
# show()
