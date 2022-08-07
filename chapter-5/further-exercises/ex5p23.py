import sys
sys.path.insert(0,'Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from numpy import loadtxt, shape, zeros, sqrt, cos, sin, amax
from pylab import imshow, show, figure, plot, gray, colorbar, clim
from math import pi
def grad2d(image, h):
    #Determine number of rows and columns
    Nx, Ny = shape(image)

    #Initialize the two derivatives
    Dx = zeros([Nx, Ny])
    Dy = zeros([Nx, Ny])

    #Calculate the derivatives along the x-direction
    Dx[1:(Nx-1),:] = -(image[2:Nx,:] - image[0:(Nx-2),:])/(2*h)
    Dx[0,:] = -(image[1,:]-image[0,:])/h
    Dx[Nx-1,:] = -(image[Nx-1,:] - image[Nx-2,:])/h

    #Calculate the derivatives along the y-direction
    Dy[:,1:(Ny-1)] = -(image[:,2:Ny]-image[:,0:(Ny-2)])/(2*h)
    Dy[:,0] = -(image[:,1]-image[:,0])/h
    Dy[:,Ny-1] = -(image[:,Ny-1]-image[:,Ny-2])/h

    return Dx, Dy

def reliefMap(Dx,Dy,phi):
    Intensity = - (cos(phi)*Dx + sin(phi)*Dy)/sqrt(Dx**2+Dy**2+1)
    return Intensity

altitude = loadtxt("altitude.txt",float)

#part a: Use central difference in the middle (30/40000 on the order of 10^-4)
#Use forward difference on the left and bottom edges
#Use backward difference on the top and right edges

#Determine number of rows and columns
# Nx, Ny = shape(altitude)

#Step size is ~30 km
# h = 30000

#Initialize the two derivatives
# Dx = zeros([Nx, Ny])
# Dy = zeros([Nx, Ny])

#Calculate the derivatives along the x-direction
# Dx[1:(Nx-1),:] = (altitude[2:Nx,:] - altitude[0:(Nx-2),:])/(2*h)
# Dx[0,:] = (altitude[1,:]-altitude[0,:])/h
# Dx[Nx-1,:] = (altitude[Nx-1,:] - altitude[Nx-2,:])/h

#Calculate the derivatives along the y-direction
# Dy[:,1:(Ny-1)] = (altitude[:,2:Ny]-altitude[:,0:(Ny-2)])/(2*h)
# Dy[:,0] = (altitude[:,1]-altitude[:,0])/h
# Dy[:,Ny-1] = (altitude[:,Ny-1]-altitude[:,Ny-2])/h

#Part b: Plot the relief map
#Step size is ~30 km
h = 30000
phi = pi/4
dwdx, dwdy = grad2d(altitude,h)
Intensity = reliefMap(dwdx,dwdy,phi)
Intensityn = Intensity/amax(abs(Intensity))
fig1 = figure(1)
imshow(altitude)
colorbar()

fig2 = figure(2)
imshow(Intensityn)
gray()
colorbar()
clim(-1,1)
show()

#Part c
h = 2.5
phi_stm = pi/3
stm  = loadtxt('stm.txt',float)
Dx_stm, Dy_stm = grad2d(stm, h)
Intensity_stm = reliefMap(Dx_stm, Dy_stm, phi_stm)

fig3 = figure(3)
imshow(stm)
colorbar()

fig4 = figure(4)
imshow(Intensity_stm/amax(abs(Intensity_stm)))
colorbar()
show()
