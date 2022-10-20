from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4

from numpy import sin, linspace, empty, transpose, array, pi, sqrt, cos
from pylab import plot, xlabel, ylabel, show, legend, xlim
from vpython import sphere, vector, rate, cylinder

g = 9.81
l = 0.1
C = 2
Omega = 5 #First value in book
Omega = 0.958*sqrt(g/l) #Small angle resonant frequency is sqrt(g/l)
# Omega = sqrt(g/l)
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta) + C*cos(theta)*sin(Omega*t)
    return array([ftheta, fomega],float)

a = 0.0
b = 100.0
# b = 10*2*pi*sqrt(l/g)
N = 5000
t = linspace(a,b,N)
theta0 = 0
x0 = array([theta0, 0], float)
t0 = 0

x_sol = rk4(f,t,x0,t0)
plot(t,transpose(x_sol[0,:]/pi))
xlabel('Time (sec)')
ylabel('Theta(t)')
show()

# Generate animation of spheres
# pxt = l*sin(x_sol[0,0])
# pzt = l*cos(x_sol[0,0])
# mass = sphere(pos=vector(pzt,pxt,0),radius=0.01)
# rod = cylinder(pos=vector(0,0,0),axis=vector(pzt,pxt,0),radius=0.0025)
# for tt in range(1,N):
#     rate(30)
#     th = x_sol[0,tt]
#     pxt = l*sin(th)
#     pzt = l*cos(th)
#     mass.pos=vector(pxt,-pzt,0)
#     rod.axis=vector(pxt,-pzt,0)
