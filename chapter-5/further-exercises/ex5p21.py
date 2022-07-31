import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from numpy import linspace, meshgrid, sqrt, ones, zeros, transpose, sin
from math import pi
from physical_constant import free_space_permittivity
from pylab import imshow, show, colorbar, clim, figure, streamplot, contour
from numDiff import finiteDiff
from numInt import gaussQuadInt2D

dx = 0.01;
dy = 0.01;
Dx = 1
Dy = 1

x1 = -5*10**-2
y1 = 0
x2 = 5*10**-2
y2 = 0
q1 = 1*10**-10
q2 = -1*10**-10
e0 = free_space_permittivity()

Nx = round(Dx/dx)+1
Ny = round(Dy/dy)+1
xx = linspace(-Dx/2,Dx/2,Nx)
yy = linspace(-Dy/2,Dy/2,Ny)

#Generate  and plot potential function
[X,Y] = meshgrid(xx,yy)
def Phi(x,y):
    return 1/(4*pi*e0)*(q1/sqrt((x-x1)**2+(y-y1)**2)+q2/sqrt((x-x2)**2+(y-y2)**2))
fig1 = figure(1)
imshow(Phi(X,Y),extent = [-Dx/2, Dx/2, -Dy/2, Dy/2])
colorbar()
clim(-20, 20)
contour(X,Y,Phi(X,Y),linspace(-10,10,11),alpha = 0.5, colors = 'k')

#Generate electric field vector components
Ex = zeros([Nx, Ny])
Ey = zeros([Nx, Ny])
for kk in range(Nx):
    def Phix(x):
        return Phi(x,Y[:,kk])
    Ex[:,kk] = finiteDiff(Phix,X[:,kk], h = 10**-6)

for kk in range(Nx):
    def Phiy(y):
        return Phi(X[kk,:],y)
    Ey[kk,:] = finiteDiff(Phiy,Y[kk,:], h = 10**-6)
# fig2 = figure(2)
streamplot(X,Y,-Ex,-Ey,color ='r',density = 0.75, linewidth = 0.5)
show()

#Part c:
L = 0.1
q0 = 100
def sigma(x,y):
    return q0*sin(2*pi*x/L)*sin(2*pi*y/L)

def integrand(xp,yp):
    return sigma(xp,yp)/sqrt((X-xp)**2 + (Y-yp)**2)
Phi_distribution = 1/(4*pi*e0)*gaussQuadInt2D(integrand,-L/2,L/2,-L/2,L/2,100)

def Fx(x):
    def integrandx(xp,yp):
        return sigma(xp,yp)/sqrt((x-xp)**2 + (Y-yp)**2)
    return 1/(4*pi*e0)*gaussQuadInt2D(integrandx,-L/2,L/2,-L/2,L/2,100)

def Fy(y):
    def integrandy(xp,yp):
        return sigma(xp,yp)/sqrt((X-xp)**2 + (y-yp)**2)
    return 1/(4*pi*e0)*gaussQuadInt2D(integrandy,-L/2,L/2,-L/2,L/2,100)

Ex_distribution = finiteDiff(Fx,X,h=10**-4, type='central')
Ey_distribution = finiteDiff(Fy,Y,h=10**-4, type='central')

fig2 = figure(2)
imshow(Phi_distribution,extent = [-Dx/2, Dx/2, -Dy/2, Dy/2])
colorbar()
contour(X,Y,Phi_distribution,linspace(-1*10**10,1*10**10,11),alpha = 0.5, colors = 'k')
streamplot(X,Y,-Ex_distribution,-Ey_distribution,color ='b',density = 0.75, linewidth = 0.5)
show()
