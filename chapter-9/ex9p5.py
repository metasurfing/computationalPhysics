from numpy import empty, zeros, arange, exp
from pylab import plot,xlabel,ylabel,show
from vpython import curve, vector, rate

#Constants
L = 1
C = 1
d = 0.1
sigma = 0.3
N = 100
a = L/N
v = 100
h = 1e-6
epsilon = h/1000
x = arange(0,L,L/(N+1))

tend = 1 + epsilon

#Create arrays
Phi = zeros(N+1, float)
Phip = empty(N+1,float)
Psi = C/L**2 * x*(L-x)/L**2 * exp(-(x-d)**2/2/sigma**2)
Psip = empty(N+1, float)


#Main loop
t = 0.0
string = curve(vector(x[0],Phi[0],0),vector(x[1],Phi[1],0))
scale = 500
for ii in range(2,N+1):
    string.append(vector(x[ii],Phi[ii],0))

count = 0
while t<tend:
    count += 1
    #Calculate the new values of Phi and Psi
    Phip[1:N] = Phi[1:N] + h * Psi[1:N]
    Psip[1:N] = Psi[1:N] + h * (v/a)**2 * (Phi[2:N+1] + Phi[0:N-1] - 2*Phi[1:N])
    Phi,Phip = Phip,Phi
    Psi, Psip = Psip,Psi
    t += h
    # if count%1 == 0:
    rate(1000)
    for ii in range(0,N+1):
        # string.modify(ii,y=scale*Phi[ii])
        string.modify(ii,y=scale*Phi[ii])
