from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from physical_constant import sun_mass, Newton_Gravity
from numpy import sqrt, array, empty, append, linalg, size
from pylab import plot, axis, show, figure
from math import inf
a = 1
b = 3
nvars = 2

def f(r):
    x = r[0]
    y = r[1]

    fx = 1 - (b+1)*x + a*(x**2)*y
    fy = b*x - a*(x**2)*y

    return array([fx, fy], float)

def step(r,H,t,delta):
    #Initialize counter
    n = 1

    #Take first euler step to launch modified midpoint method
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    #Set up Richardson Extrapolation
    R1 = empty([1,nvars],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
    error = 2*delta*H
    while n <= 8 and error > delta*H and error < inf:
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

        #Richardson extrapolation for nth step
        for mm in range(1,n):
            epsilon = (R1[mm-1] - R2[mm-1])/((n/(n-1))**(2*mm)-1)
            R1[mm] = R1[mm-1] + epsilon
        error = linalg.norm(epsilon)

    if error>delta*H:
        #Split step in half
        ro1, to1 = step(r,H/2,t,delta)
        #Check sizes so that append works properly and indexing doesn't throw an error
        if size(ro1)>nvars:
            #Solve second half of interval
            ro2, to2 = step(ro1[-1,:],H/2,t+H/2,delta)
            if size(ro2)>nvars:
                rout = append(ro1,ro2,axis=0)
                tout = append(to1,to2)
            else:
                rout = append(ro1,[ro2],axis=0)
                tout = append(to1,to2)

        else:
            #Solve second half of interval
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
tf = 20
H0 = tf - t0
delta = 1e-10
r0 = array([0,0],float)

r_sol, t_sol = step(r0,H0,t0,delta)

figure(1)
plot(t_sol,r_sol[:,0])
plot(t_sol,r_sol[:,0],'o')

plot(t_sol,r_sol[:,1])
plot(t_sol,r_sol[:,1],'o')

figure(2)
plot(t_sol[1::]-t_sol[0:-1])
show()
