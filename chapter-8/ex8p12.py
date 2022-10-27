from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from ode import verlet
from numpy import sqrt, array, linalg
from physical_constant import Newton_Gravity, sun_mass, earth_mass
from pylab import plot, show, axis, figure, legend, xlabel

G = Newton_Gravity()
M = sun_mass()
m = earth_mass()

def f(x,t):
    r = sqrt(sum(x**2))
    return -G*M*x/r**3

t0 = 0
tf = 24*60*60*360*4
t = [t0, tf]
x0 = array([-1.4710*1e11, 0],float)
v0 = array([0, 3.0287e4], float)
h = 60*60

[x_sol, v_sol, t_sol] = verlet(f,t,x0,v0,t0,h)

r = linalg.norm(x_sol,axis=0)
v = linalg.norm(v_sol,axis=0)

potE = -G*M*m/r
kinE = 1/2*m*v**2
totE = potE + kinE

figure(1)
plot(x_sol[0,:],x_sol[1,:])
axis('equal')
figure(2)
plot(t_sol,potE)
plot(t_sol,kinE)
plot(t_sol,totE)
legend(['Potential Energy','Kinetic Energy','Total Energy'])
xlabel('Time (sec)')
figure(3)
plot(t_sol,totE)
show()
