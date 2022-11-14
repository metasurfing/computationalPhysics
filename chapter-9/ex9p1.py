from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from physical_constant import free_space_permittivity
from numpy import empty, zeros, max
from pylab import imshow, gray, show, figure


#Constants
M = 100
target = 1e-6
a = 0.01
e0 = free_space_permittivity()
an = a/e0 #Normalization cancels with change of units for charge density
          #so it is better to not include the e0 changes

#Array to hold potential values
phi = zeros([M+1, M+1],float)
phi_prime = empty([M+1,M+1],float)
phi_prime[0,:] = phi[0,:]
phi_prime[M,:] = phi[M,:]
phi_prime[:,0] = phi[:,0]
phi_prime[:,M] = phi[:,M]

#Build array for the charge density in the interior
rho_xy = zeros([M-1,M-1],float)
rho_xy[60:81,20:41] = -1
rho_xy[20:41,60:81] = 1
# figure(1)
# imshow(rho_xy)
# show()

#Main loop
delta = 1.0

while delta>target:

    phi_prime[1:M,1:M] = 0.25*(phi[2:(M+1),1:M] + phi[0:(M-1),1:M] + \
                                phi[1:M,2:(M+1)] + phi[1:M,0:(M-1)]) + \
                                rho_xy*(a**2)/4

    delta = max(abs(phi-phi_prime))

    phi, phi_prime = phi_prime, phi

imshow(phi)
gray()
show()
