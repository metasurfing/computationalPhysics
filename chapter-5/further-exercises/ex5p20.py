import sys
from numpy import linspace, sin, zeros
from pylab import plot, show
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from numInt import trapInt1D, gaussQuadInt1D
#Part b:
#It takes in the function values in order to avoid recalculating function values
#every time the function is called recursively
def sinc2(x):
    if x != 0:
        return (sin(x)/x)**2
    else:
        return 1

a = 0
b = 10
AbsTol = 10**-4
# I = trapInt1D(sinc2,a,b,opt='non-uniform',AbsTol = 10**-4)
# print(I)

Ig = gaussQuadInt1D(sinc2,a,b,200)
print(Ig)
Xm = []
Xm.append(a)
Xm.append(b)

def step(x1,x2,f1,f2):
    h = x2-x1
    xm = 0.5*(x1+x2)
    fm = sinc2(xm);
    Xm.append(xm)

    I1 = 0.5*h*(f1 + f2)
    I2 = 0.25*h*(f1 + 2*fm + f2)
    if 1/3*abs(I2-I1) < AbsTol:
        return 1/6*h*(f1 + 4*fm + f2)
    else:
        return step(x1,xm,f1,fm) + step(xm, x2, fm, f2)

I = step(a,b,sinc2(a),sinc2(b))
print(I)

Nx = 101
xx = linspace(a,b,Nx)
Ix = zeros(Nx)
Ixm = zeros(len(Xm))
for kk in range(Nx):
    Ix[kk] = sinc2(xx[kk])

for kk in range(len(Xm)):
    Ixm[kk] = sinc2(Xm[kk])

plot(xx,Ix)
plot(Xm,Ixm,'o',markersize = 3)
show()
