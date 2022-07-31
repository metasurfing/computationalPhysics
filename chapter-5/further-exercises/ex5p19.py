import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from numInt import gaussQuadInt1D
from math import pi, ceil
from numpy import exp, sin, sqrt, linspace, zeros, transpose
from pylab import figure, plot, show, xlabel, ylabel, imshow, gray

#Part a: the spacing is d = pi/alpha

#Part b:
d = 20*10**-6
def q(u):
    alpha = pi/d
    return sin(alpha*u)**2
fd = 1/2/d
# print(fd)

#part e:
def qi(u):
    alpha = pi/d
    beta = 0.5*alpha
    return sin(alpha*u)**2 * sin(beta*u)**2

def qii(u):
    #slit 1
    if u >= -45*10**-6 and u <= -35*10**-6:
        return 1
    elif u <= 45*10**-6 and u >= 25*10**-6:
        return 1
    else:
        return 0

#Part c
l0 = 500*10**-9

f = 1
W = 10*d;
Wx = 10*10**-2
# Np = ceil(2*fd*W/d)
# print(Np)
Np = 200
Nx = 2001
u = linspace(-W/2, W/2, Np)
xx = linspace(-Wx/2, Wx/2, Nx)

def I(x):
    def integrand(u):
        return sqrt(q(u))*exp(2j*pi*x*u/(l0*f))
    return abs(gaussQuadInt1D(integrand,-W/2,W/2,Np))**2

def Ii(x):
    def integrand(u):
        return sqrt(qi(u))*exp(2j*pi*x*u/(l0*f))
    return abs(gaussQuadInt1D(integrand,-W/2,W/2,Np))**2

def Iii(x):
    def integrand(u):
        return sqrt(qii(u))*exp(2j*pi*x*u/(l0*f))
    return abs(gaussQuadInt1D(integrand,-W/2,W/2,Np))**2

Nk = 300
Intensity = zeros([Nk,Nx])
Intensityi = zeros([Nk,Nx])
Intensityii = zeros([Nk,Nx])

Intensity[0,:] = I(xx)
Intensityi[0,:] = Ii(xx)
Intensityii[0,:] = Iii(xx)

for kk in range(Nk):
    Intensity[kk,:] = Intensity[0,:]
    Intensityi[kk,:] = Intensityi[0,:]
    Intensityii[kk,:] = Intensityii[0,:]

# fig1 = figure(1)
# plot(u,q(u))
fig2 = figure(2)
imshow(Intensity)

fig3 = figure(3)
imshow(Intensityi)

fig4 = figure(4)
imshow(Intensityii)
# plot(xx,Intensity)
show()
