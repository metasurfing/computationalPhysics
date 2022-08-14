from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from linearAlg import gaussElim
from numpy import array, zeros, empty, arange, cos
from vpython import sphere, vector, rate

omega = 2
mass = 1
k = 6
N = 26
C = 1

alpha = 2*k - mass*omega**2

A = zeros([N,N],float)
f = zeros(N,float)
f[1] = C

A[0,0] = alpha - k
A[0,1] = -k
A[N-1,N-1] = alpha -k
A[N-1,N-2] = -k

for kk in range(1,N-1):
    A[kk,kk] = alpha
    A[kk,kk-1] = -k
    A[kk,kk+1] = -k

x = gaussElim(A,f,opts = 'banded',above=1,below=1)

#Generate animation of spheres
masses = empty(N,sphere)
px = empty(N,float)
#mass separation
d = 1.5

for nn in range(N):
    px[nn] = (nn-N/2)*d
    masses[nn] = sphere(pos=vector(px[nn]+x[nn],0,0),radius=0.4)

for t in arange(0,20,0.05):
    rate(30)
    pxt = px + x*cos(omega*t)
    for nn in range(N):
        masses[nn].pos = vector(pxt[nn],0,0)
