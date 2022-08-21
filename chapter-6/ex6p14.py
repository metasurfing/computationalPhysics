from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from nlsolve import binary_search
from numpy import tan, sqrt, arange, empty
from physical_constant import electron_mass, electron_charge, Planck_bar
from pylab import plot, show, xlabel, ylabel, ylim

eV = -electron_charge()

m = electron_mass()
h_bar = Planck_bar()

V = 20*eV
w = 1e-9

def y1(E):
    return tan(sqrt(w**2*m*E/2/h_bar**2))
def y2(E):
    return sqrt((V-E)/E)
def y3(E):
    return -sqrt(E/(V-E))

Es = arange(0.01*eV, 19.99*eV, 0.1*eV)

plot(Es,y1(Es))
plot(Es,y2(Es))
plot(Es,y3(Es))
ylim(-50,50)
show()
a = empty(6,float)
b = empty(6,float)
a[0] = 1*eV #odd
a[1] = 1.5*eV #even
a[2] = 4*eV #odd
a[3] = 5*eV #even
a[4] =10*eV #odd
a[5] = 12.5*eV #even
b[0] = 2.5*eV
b[1] = 3*eV
b[2] = 7.5*eV
b[3] = 8.5*eV
b[4] = 15*eV
b[5] = 17*eV

errorTol = 0.001*eV

Estates = empty(6,float)

def fodd(E):
    return y1(E) - y3(E)
def feven(E):
    return y1(E) - y2(E)
# plot(Es/eV,feven(Es))
# ylim(-10,10)
show()
for kk in range(6):
    if kk%2 == 0:
        Estates[kk] = binary_search(fodd,a[kk],b[kk],tol = errorTol)
    else:
        Estates[kk] = binary_search(feven,a[kk],b[kk],tol = errorTol)

print(Estates/eV)
