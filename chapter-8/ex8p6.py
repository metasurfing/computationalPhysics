from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4

from numpy import sin, linspace, empty, transpose, array, pi, sqrt, cos
from pylab import plot, xlabel, ylabel, show, legend, xlim
from vpython import sphere, vector, rate, cylinder

omega = 1
def f(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega**2*x**3 # part c
    # fy = -omega**2*x #parts a and b
    return array([fx, fy],float)

a = 0.0
b = 50.0
# b = 10*2*pi*sqrt(l/g)
N = 5000
t = linspace(a,b,N)
theta0 = 0
x0 = array([1, 0], float)
t0 = 0

x_sol2 = rk4(f,t,x0*2,t0)
x_sol1 = rk4(f,t,x0,t0)
# plot(t,transpose(x_sol1[0,:]))
# plot(t,transpose(x_sol2[0,:]))
plot(transpose(x_sol1[1,:]),transpose(x_sol1[0,:]))
plot(transpose(x_sol2[1,:]),transpose(x_sol2[0,:]))
xlabel('x_dot(t)')
# xlabel('Time (sec)')
ylabel('x(t)')
show()

#Van der pol oscillator
omega = 1
mu = 1
def f1(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu*(1-x**2)*y-omega**2*x
    return array([fx, fy],float)

mu2 = 2
def f2(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu2*(1-x**2)*y-omega**2*x
    return array([fx, fy],float)

mu3 = 4
def f3(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu3*(1-x**2)*y-omega**2*x
    return array([fx, fy],float)


a = 0.0
b = 20.0
# b = 10*2*pi*sqrt(l/g)
N = 10000
t = linspace(a,b,N)
theta0 = 0
x0 = array([1, 0], float)
t0 = 0

x_sol1 = rk4(f1,t,x0,t0)
x_sol2 = rk4(f2,t,x0,t0)
x_sol3 = rk4(f3,t,x0,t0)
# plot(t,transpose(x_sol1[0,:]))
# plot(t,transpose(x_sol2[0,:]))
plot(transpose(x_sol1[1,:]),transpose(x_sol1[0,:]))
plot(transpose(x_sol2[1,:]),transpose(x_sol2[0,:]))
plot(transpose(x_sol3[1,:]),transpose(x_sol3[0,:]))
xlabel('x_dot(t)')
# xlabel('Time (sec)')
ylabel('x(t)')
legend(['mu = 1','mu = 2', 'mu = 3'])
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
