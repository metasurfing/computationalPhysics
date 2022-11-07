from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from physical_constant import sun_mass, Newton_Gravity
from numpy import sqrt, array, empty, append, linalg, size
from pylab import plot, axis, show, figure
G = Newton_Gravity()
M = sun_mass()

def f(r):

    x = r[0]
    xdot = r[1]
    y = r[2]
    ydot = r[3]
    rad = sqrt(x**2 + y**2)

    fx = xdot
    fxdot = -G*M/rad**2 * (x/rad)
    fy = ydot
    fydot = -G*M/rad**2 * (y/rad)

    return array([fx, fxdot, fy, fydot], float)

def step(r,H,t,delta):
    #Initial counter
    n = 1
    nvars = 4

    #Take first euler step to launch modified midpoint method
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    #Set up Richardson Extrapolation
    R1 = empty([1,nvars],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
    error = 2*delta*H
    while n <= 8 and error > delta*H:
        n += 1
        h = H/n

        #Modified Midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for ii in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)

        R2 = R1.copy()
        R1 = empty([n,nvars],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))

        for mm in range(1,n):
            epsilon = (R1[mm-1] - R2[mm-1])/((n/(n-1))**(2*mm)-1)
            R1[mm] = R1[mm-1] + epsilon
        error = linalg.norm(epsilon[::2])

    if error>delta*H:
        ro1, to1 = step(r,H/2,t,delta)
        if size(ro1)>nvars:
            ro2, to2 = step(ro1[-1,:],H/2,t+H/2,delta)
            if size(ro2)>nvars:
                rout = append(ro1,ro2,axis=0)
                tout = append(to1,to2)
            else:
                rout = append(ro1,[ro2],axis=0)
                tout = append(to1,to2)

        else:
            ro2, to2 = step(ro1,H/2,t+H/2,delta)
            if size(ro2)>nvars:
                rout = append([ro1],ro2,axis=0)
                tout = append(to1,to2)
            else:
                rout = append([ro1],[ro2],axis=0)
                tout = append(to1,to2)

    else:
        rout = R1[n-1]
        tout = t+H

    return rout, tout


t0 = 0
tf = 2.1*1e9
H0 = tf - t0
delta = 1e3/(365*24*60*60)
r0 = array([4*1e12, 0, 0, 500],float)

r_sol, t_sol = step(r0,H0,t0,delta)

figure(1)
plot(r_sol[:,2],r_sol[:,0])
plot(r_sol[:,2],r_sol[:,0],'o')
axis('equal')

figure(2)
plot(t_sol[1::]-t_sol[0:-1])
show()
