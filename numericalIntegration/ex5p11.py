import numInt as ni
from math import sin, cos, sqrt, pi
from numpy import linspace, zeros
import pylab as plt

def c(t):
    return cos(0.5*pi*t**2)

def s(t):
    return sin(0.5*pi*t**2)

lam = 1
z = 3
N = 50
I0 = 1

def u(x):
    return x*sqrt(2/(lam*z))

xpos = linspace(-5,5,200)
I = zeros(len(xpos))

xk, wk = ni.gaussxw(N)

for kk in range(len(xpos)):
    u_cur = u(xpos[kk])
    xk_cur = 0.5*u_cur*xk + 0.5*u_cur
    wk_cur = 0.5*u_cur*wk

    Cu = ni.gaussQuadInt1D(c, 0, u_cur, N, xk_cur, wk_cur)
    Su = ni.gaussQuadInt1D(s, 0, u_cur, N, xk_cur, wk_cur)

    I[kk] = I0/8*((2*Cu+1)**2+(2*Su+1)**2)

f1 = plt.figure(1)
plt.plot(xpos,I)
plt.xlabel('x position (m)')
plt.ylabel('Intensity')
plt.show()
