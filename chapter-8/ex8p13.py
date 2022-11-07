from time import perf_counter
from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
from ode import burlisch_stoer
from numpy import empty, linspace, array, sqrt, abs, amin, rint, append, reshape, transpose
from physical_constant import Newton_Gravity, sun_mass
from pylab import plot, show, xlabel, ylabel, figure, axis, figure


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

def fp(r,t):
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

t0 = 0
tf = 24*60*60*365
tfp = 24*60*60*365*250*(1+1/4/365)
tfp = 2*1e9
t = [t0, tf]
tp = [t0, tfp]
x0 = array([-1.4710*1e11, 0, 0, 3.0287e4],float)
xp0 = array([-4.4368*1e12, 0, 0, 6.1218e3],float)
H = 60*60*24*7
Hp = 60*60*24*7*5
delta = 1e3/(60*60*24*365)

x_sol = burlisch_stoer(f,t,x0,t0,H=H,delta=delta)
x_solp = burlisch_stoer(fp,tp,xp0,t0,H=Hp,delta=delta)

figure(1)
plot(x_sol[:,0],x_sol[:,2])
axis('equal')
figure(2)
plot(x_solp[:,0],x_solp[:,2])
axis('equal')
show()
