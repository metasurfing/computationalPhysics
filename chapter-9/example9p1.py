from numpy import empty, zeros, max
from pylab import imshow, gray, show

#Constants
M = 100
V = 1.0
target = 1e-6

#Array to hold potential values
phi = zeros([M+1, M+1],float)
phi[0,:] = V
phi_prime = empty([M+1,M+1],float)
phi_prime[0,:] = phi[0,:]
phi_prime[M,:] = phi[M,:]
phi_prime[:,0] = phi[:,0]
phi_prime[:,M] = phi[:,M]

#Main loop
delta = 1.0

while delta>target:

    phi_prime[1:M,1:M] = 0.25*(phi[2:(M+1),1:M] + phi[0:(M-1),1:M] + \
                                phi[1:M,2:(M+1)] + phi[1:M,0:(M-1)])

    delta = max(abs(phi-phi_prime))

    phi, phi_prime = phi_prime, phi

imshow(phi)
gray()
show()
