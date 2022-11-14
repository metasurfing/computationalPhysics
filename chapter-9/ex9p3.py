from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numpy import empty, zeros, max
from pylab import imshow, gray, show, figure
from time import perf_counter

#Constants
M = 100
target = 1e-6


#Array to hold potential values
phi = zeros([M+1, M+1],float)
phi_prime = empty([M+1,M+1],float)
phi_prime[0,:] = phi[0,:]
phi_prime[M,:] = phi[M,:]
phi_prime[:,0] = phi[:,0]
phi_prime[:,M] = phi[:,M]

#Assign potential to the plates
phi[19:80,19] = 1.0
phi[19:80,79] = -1.0

figure(1)
imshow(phi)
show()

#Main loop
delta = 1.0

#Vectorized Jacobi
tic = perf_counter()
while delta>target:

    phi_prime[1:M,1:M] = 0.25*(phi[2:(M+1),1:M] + phi[0:(M-1),1:M] + \
                                phi[1:M,2:(M+1)] + phi[1:M,0:(M-1)])
    phi_prime[19:80,19] = 1.0
    phi_prime[19:80,79] = -1.0

    delta = max(abs(phi-phi_prime))

    phi, phi_prime = phi_prime, phi
toc = perf_counter()
print('Vectorized Jacobi took:',toc-tic, 'seconds to finish.')
imshow(phi)
gray()
show()

#Gauss-Seidel

#Array to hold potential values
phi = zeros([M+1, M+1],float)
#Assign potential to the plates
phi[19:80,19] = 1.0
phi[19:80,79] = -1.0

phi_prime = phi.copy()
omega = 0.935
delta = 1.0
tic = perf_counter()
while delta>target:
    for ii in range(1,M):
        for jj in range(1,M):
            if not((ii>=19 and ii<80) and (jj == 19 or jj == 79)):
                phi[ii,jj] = (1+omega)*0.25*(phi[ii-1,jj] + phi[ii+1,jj] + \
                                        phi[ii,jj-1] + phi[ii,jj+1]) - \
                                        omega*phi[ii,jj]

    delta = max(abs(phi-phi_prime))
    phi_prime = phi.copy()

toc = perf_counter()
print('Gauss-Seidel with omega:', omega, 'took' ,toc - tic ,'seconds to finish.')

imshow(phi)
gray()
show()
