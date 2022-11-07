from time import perf_counter
from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from ode import rk4
from numpy import empty, linspace, array, sqrt, abs, amin, rint, append, reshape, transpose
from physical_constant import Newton_Gravity, sun_mass
from pylab import plot, show, xlabel, ylabel, figure, axis


G = Newton_Gravity()
M = sun_mass()

def f(r,t):
    x = r[0]
    xdot = r[1]
    y = r[2]
    ydot = r[3]
    r = sqrt(x**2 + y**2)

    fx1 = xdot
    fx2 = -G*M*x/r**3
    fx3 = ydot
    fx4 = -G*M*y/r**3

    return array([fx1, fx2, fx3, fx4],float)

x0 = [4e12, 0, 0, 500]
t0 = 0.0
tf = 60*60*24*365*50*2
print(tf)
t = [t0, tf]
h = 60*60*3
# tic = perf_counter()
# x_sol = rk4(f,t,x0,t0,h,'fixed')
# toc = perf_counter()
# print(toc-tic)
#A fixed step size of 3 hours provides reasonable accuracy over two periods.
#Larger step sizes cause the orbit to quickly diverge. The integration took
#approximately 4.5 seconds.

delta = 1e3/(365*60*60*24)
tcur = t0
x0cur = x0.copy()
h = 60*60*365*24
tarray = array(t0,float)
x_sol = array(x0cur,float)
tic = perf_counter()
while tcur < tf:
    hp = 2*h
    t_tmp = [tcur, tcur+hp]
    x_solh = rk4(f,t_tmp,x0cur,tcur,h,'fixed')
    x_solhp = rk4(f,t_tmp,x0cur,tcur,hp,'fixed')

    epsx = 1/30*abs(x_solh[0,2]-x_solhp[0,1])
    epsy = 1/30*abs(x_solh[2,2]-x_solhp[2,1])

    if epsx <= 1e-16 and epsy <= 1e-16:
        rho = 30*h*delta/sqrt(2e-16)
    else:
        rho = 30*h*delta/sqrt(epsx**2 + epsy**2)
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
        x_sol = append(x_sol,x0cur)
    else:
        h *= rho**(1/4)
toc = perf_counter()

print(toc-tic)
Nt_adaptive = len(x_sol)//4
x_sol = transpose(reshape(x_sol, [Nt_adaptive,4]))

figure(1)
#Plot orbit
plot(x_sol[2,:],x_sol[0,:])
plot(x_sol[2,:],x_sol[0,:],'o')
axis('equal')

figure(2)
#Plot step size versus step
plot(tarray[1:(Nt_adaptive-1)]-tarray[0:(Nt_adaptive-2)])
show()
