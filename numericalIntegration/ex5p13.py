from math import sqrt, pi, factorial, cos, tan
from numpy import linspace, zeros, exp
from pylab import plot, figure, show
from numInt import gaussxwab, gaussQuadInt1D

#Parts a & b
def H(x,N):
    Hnm1 = 1
    Hn = 2*x
    if N == 0:
        Hnp1 = Hnm1
    elif N == 1:
        Hnp1 = Hn
    else:
        for nn in range(1,N):
            Hnp1 = 2*x*Hn - 2*nn*Hnm1
            Hnm1 = Hn
            Hn = Hnp1
    return Hnp1

Nx = 1001
#N = 30
#x = linspace(-10,10,Nx)
N = 3
x = linspace(-4,4,Nx)
Hn = zeros([N+1, Nx])
Phi = zeros([N+1, Nx])
Exp_mx2 = exp(-(x**2)/2);
for nn in range(N+1):
    Hn[nn,:] = H(x,nn)
    Phi[nn,:] = 1/sqrt(2**nn*factorial(nn)*sqrt(pi))*Exp_mx2*Hn[nn,:]

f1 = figure(1)
plot(x,Hn[0,:])
plot(x,Hn[1,:])
plot(x,Hn[2,:])
plot(x,Hn[3,:])

f2 = figure(2)
for nn in range(N+1):
    plot(x,Phi[nn,:])
show()

#Part c
print('starting part c')
Ni = 100
n = 5
a = -pi/2
b = pi/2



def H(x,N=5):
    Hnm1 = 1
    Hn = 2*x
    if N == 0:
        Hnp1 = Hnm1
    elif N == 1:
        Hnp1 = Hn
    else:
        for nn in range(1,N):
            Hnp1 = 2*x*Hn - 2*nn*Hnm1
            Hnm1 = Hn
            Hn = Hnp1
    return Hnp1

def phi_n(x,N=5):
    return 1/sqrt(2**N*factorial(N)*sqrt(pi))*exp(-(x**2)/2)*H(x,N)

def integrand(z,N=5):
    return (tan(z)**2)*(abs(phi_n(tan(z),N))**2)/(cos(z)**2)

s = gaussQuadInt1D(integrand,a,b,Ni)
print(sqrt(s))
