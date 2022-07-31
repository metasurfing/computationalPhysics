import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from numpy import linspace, meshgrid, sqrt, ones, zeros, transpose
from math import pi
from physical_constant import free_space_permittivity
from pylab import imshow, show, colorbar, clim, figure, streamplot, contour
from numDiff import finiteDiff

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
