from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from ode import rk4
from numpy import array, empty, linspace, sqrt, zeros, cos, shape, arange, pi
from pylab import plot, show, xlabel, ylabel, xlim, ylim, figure, legend
from vpython import sphere, vector, rate

omega = 2
m = 1
k = 6

#number of masses
Nm = 26

#mass separation
d = 1.5

def f(r,t):
    N = len(r)
    fx = empty(N,float)
    for nn in range(N//2):

        if nn == 0:
            Fi = cos(omega*t)
        else:
            Fi = 0

        idx = 2*nn
        idxp1 = 2*nn + 1

        fx[idx] = r[idxp1]
        if idx == 0:
            fx[idxp1] = k/m*(r[idx+2]-r[idx] - d) + Fi/m
        elif idx == N-2:
            fx[idxp1] = k/m*(r[idx-2]-r[idx] + d) + Fi/m
        else:
            fx[idxp1] = k/m*(r[idx+2] + r[idx-2] - 2*r[idx]) + Fi/m

    return fx

Nt = 500
t = linspace(0,20,Nt)
t0 = 0
x0 = zeros(2*Nm,float)
for nn in range(Nm):
    x0[2*nn] = nn*d

x = rk4(f,t,x0,t0)

#Generate animation of spheres
masses = empty(Nm,sphere)
px = x[::2,:].copy()

for nn in range(Nm):
    masses[nn] = sphere(pos=vector(px[nn,0]-Nm/2*d,0,0),radius=0.4)

for tt in range(Nt):
    rate(30)
    pxt = px[:,tt]
    for nn in range(Nm):
        masses[nn].pos = vector(pxt[nn]-Nm/2*d,0,0)
