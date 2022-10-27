from math import sin, pi
from numpy import empty,array,arange, shape
from pylab import plot,show

g = 9.81
l = 0.1
theta0 = 179*pi/180
a = 0.0
b = 10.0
N = 100
H = (b-a)/N
delta = 1e-8

def f(r):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

tpoints = arange(a,b,H)
thetapoints = []
r = array([theta0, 0.0],float)

for tt in tpoints:
    thetapoints.append(r[0])

    #Do modified midpoint step of size H to get started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    R1 = empty([1,2],float)
    R1[0] = 0.5*(r1+r2+0.5*H*f(r2))

    error = 2*H*delta

    while error > H*delta:
        n += 1
        h = H/n
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for ii in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)

        R2 = R1
        R1 = empty([n,2],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))

        for mm in range(1,n):
            epsilon = (R1[mm-1]-R2[mm-1])/((n/(n-1))**(2*mm)-1)
            R1[mm] = R1[mm-1] + epsilon

        error = abs(epsilon[0])
        print(shape(R1[mm]))


    r = R1[n-1]

plot(tpoints,thetapoints)
plot(tpoints,thetapoints,"b.")
show()
