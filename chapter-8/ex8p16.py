from time import perf_counter
from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from ode import rk4
from numpy import empty, linspace, array, sqrt, abs, amin, rint, append, reshape, transpose, amax, shape
from physical_constant import Newton_Gravity, sun_mass
from pylab import plot, show, xlabel, ylabel, figure, xlim, ylim
from vpython import sphere, vector, rate, cylinder

G = 1
m0 = 150
m1 = 200
m2 = 250


def f(r,t):

    x0 = r[0]
    xdot0 = r[1]
    y0 = r[2]
    ydot0 = r[3]
    x1 = r[4]
    xdot1 = r[5]
    y1 = r[6]
    ydot1 = r[7]
    x2 = r[8]
    xdot2 = r[9]
    y2 = r[10]
    ydot2 = r[11]

    r01 = sqrt((x0-x1)**2 + (y0-y1)**2)
    r02 = sqrt((x0-x2)**2 + (y0-y2)**2)
    r12 = sqrt((x1-x2)**2 + (y1-y2)**2)

    fx0 = xdot0
    fxdot0 = G*( m1/r01*((x1-x0)/r01)/r01+ m2/r02*((x2-x0)/r02)/r02 )
    fy0 = ydot0
    fydot0 = G*( m1/r01*((y1-y0)/r01)/r01 + m2/r02*((y2-y0)/r02)/r02 )

    fx1 = xdot1
    fxdot1 = G*( m0/r01*((x0-x1)/r01)/r01 + m2/r12*((x2-x1)/r12)/r12 )
    fy1 = ydot1
    fydot1 = G*( m0/r01*((y0-y1)/r01)/r01 + m2/r12*((y2-y1)/r12)/r12 )

    fx2 = xdot2
    fxdot2 = G*( m0/r02*((x0-x2)/r02)/r02 + m1/r12*((x1-x2)/r12)/r12 )
    fy2 = ydot2
    fydot2 = G*( m0/r02*((y0-y2)/r02)/r02 + m1/r12*((y1-y2)/r12)/r12 )

    return array([fx0, fxdot0, fy0, fydot0, fx1, fxdot1, fy1, fydot1, fx2, fxdot2, fy2, fydot2],float)

r0 = [3, 0, 1, 0, -1, 0, -2, 0, -1, 0, 1, 0]
t0 = 0.0
tf = 100.0
t = [t0, tf]

delta = 1e-4
tcur = t0
x0cur = r0.copy()
h = 0.01
tarray = array(t0,float)
x_sol = array([x0cur],float)
tic = perf_counter()
x_solh = empty([12,3],float)
x_solhp = empty([12,2],float)

lim = 0.0
while tcur < tf:
    if  tcur >= lim:
        print(tcur)
        lim += 0.1 + tcur

    hp = 2*h
    t_tmp = [tcur, tcur+hp]
    #Two - step solution
    x = x0cur.copy()
    x_solh[:,0] = x.copy()
    tm1 = t_tmp[0]
    for tt in range(1,3):
        k1 = h*f(x,tm1)
        k2 = h*f(x+0.5*k1,tm1+0.5*h)
        k3 = h*f(x+0.5*k2,tm1+0.5*h)
        k4 = h*f(x+k3, tm1+h)
        x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
        x_solh[:,tt] = x
        tm1 += h

    #One - step solution
    x = x0cur.copy()
    x_solhp[:,0] = x.copy()
    tm1 = t_tmp[0]
    k1 = hp*f(x,tm1)
    k2 = hp*f(x+0.5*k1,tm1+0.5*hp)
    k3 = hp*f(x+0.5*k2,tm1+0.5*hp)
    k4 = hp*f(x+k3, tm1+hp)
    x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
    x_solhp[:,1] = x

    epsx0 = 1/30*abs(x_solh[0,2]-x_solhp[0,1])
    epsy0 = 1/30*abs(x_solh[2,2]-x_solhp[2,1])
    epsx1 = 1/30*abs(x_solh[4,2]-x_solhp[4,1])
    epsy1 = 1/30*abs(x_solh[6,2]-x_solhp[6,1])
    epsx2 = 1/30*abs(x_solh[8,2]-x_solhp[8,1])
    epsy2 = 1/30*abs(x_solh[10,2]-x_solhp[10,1])
    epstot = amax([sqrt(epsx0**2 + epsy0**2),sqrt(epsx1**2 + epsy1**2),sqrt(epsx2**2 + epsy2**2)])

    if epstot <= 1e-16:
        rho = 30*h*delta/sqrt(2e-16)
    else:
        rho = 30*h*delta/epstot

    if rho >= 1:
        #Change current initial state to last state solved for using local extrapolation
        x0cur = x_solh[:,2] + 1/15*(x_solh[:,2]-x_solhp[:,1])
        #Increment time to finale time
        tcur += hp
        #Increase step size for next go around
        hopt = h*rho**(1/4)
        h = amin([hopt,2*h])
        #add next time stamp to array
        tarray = append(tarray, tcur)
        #add solution for state vector to array
        x_sol = append(x_sol,[x0cur],axis=0)
    else:
        h *= rho**(1/4)

toc = perf_counter()

print(toc-tic)
Nt_adaptive = len(x_sol)//12
x_sol = transpose(x_sol)

figure(1)
#Plot orbit
plot(x_sol[2,:],x_sol[0,:])
plot(x_sol[2,:],x_sol[0,:],'o')
plot(x_sol[6,:],x_sol[4,:])
plot(x_sol[6,:],x_sol[4,:],'o')
plot(x_sol[10,:],x_sol[8,:])
plot(x_sol[10,:],x_sol[8,:],'o')
ylim([-5,5])
xlim([-5,5])
figure(2)
#Plot step size versus step
plot(tarray[1:(Nt_adaptive-1)]-tarray[0:(Nt_adaptive-2)])
show()

mass0 = sphere(pos=vector(x_sol[0,0],x_sol[2,0],0),radius=0.03)
mass1 = sphere(pos=vector(x_sol[4,0],x_sol[6,0],0),radius=0.06)
mass2 = sphere(pos=vector(x_sol[8,0],x_sol[10,0],0),radius=0.09)
C = 1e-1
for tt in range(1,len(tarray)):
    h = amin([tarray[tt]-tarray[tt-1],1e-3])
    rate(C/h)
    mass0.pos=vector(x_sol[0,tt],x_sol[2,tt],0)
    mass1.pos=vector(x_sol[4,tt],x_sol[6,tt],0)
    mass2.pos=vector(x_sol[8,tt],x_sol[10,tt],0)
