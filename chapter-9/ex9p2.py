from numpy import empty, zeros, max, arange
from pylab import imshow, gray, show
from time import perf_counter

#Constants
M = 100
V = 1.0
target = 1e-6
omega = 0.94 #0.94 takes ~1.57 seconds to complete
             #for loop method with Gauss-Seidel is much slower
             #than vectorized Jacobi on this problem.
             #Vectorized Jacobi finishes in ~0.52 seconds.
             #Could potentially leverage vectorized computations by operating
             #on columns or rows at a time.

#Array to hold potential values
phi = zeros([M+1, M+1],float)
phi[0,:] = V
phi_prime = phi.copy()

#Main loop
delta = 1.0
#Iteration counter
counter = 0

w = omega
tic = perf_counter()
while delta>target:
    for ii in range(1,M):
        for jj in range(1,M):
            phi[ii,jj] = (1+w)*0.25*(phi[ii-1,jj] + phi[ii+1,jj] + \
                                    phi[ii,jj-1] + phi[ii,jj+1]) - \
                                    w*phi[ii,jj]

    delta = max(abs(phi-phi_prime))
    phi_prime = phi.copy()
    counter += 1
toc = perf_counter()
print('Omega:', w, 'required' ,toc - tic ,'seconds to finish.')
print(counter)
imshow(phi)
gray()
show()
