from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from ode import rk4
from numpy import sin,cos,pi,arange, array, shape
from physical_constant import standard_gravity
from pylab import plot, show
from vpython import sphere, vector, rate, cylinder

g = standard_gravity()
m = 1
l = 0.4

def f(r,t):
    theta1 = r[0]
    omega1 = r[1]
    theta2 = r[2]
    omega2 = r[3]
    ftheta1 = omega1
    fomega1 = -(omega1**2*sin(2*theta1-2*theta2) + 2*omega2**2*sin(theta1-theta2) \
                + g/l*(sin(theta1-2*theta2)+3*sin(theta1)))/(3-cos(2*theta1-2*theta2))
    ftheta2 = omega2
    fomega2 = (4*omega1**2*sin(theta1-theta2)+omega2**2*sin(2*theta1-2*theta2) \
                + 2*(g/l)*(sin(2*theta1-theta2)-sin(theta2)))/(3-cos(2*theta1-2*theta2))
    return array([ftheta1,fomega1,ftheta2,fomega2],float)

theta0 = array([pi/2, 0, pi/2, 0],float)
t0 = 0
tf = 100
Nt = 52000
h = (tf-t0)/Nt
t = arange(t0,tf,h)

r_sol = rk4(f,t,theta0,t0)


T = m*l**2*(r_sol[1,:]**2 + 0.5*r_sol[3,:]**2 + r_sol[1,:]*r_sol[3,:]*cos(r_sol[0,:]-r_sol[2,:]))
V = -m*g*l*(2*cos(r_sol[0,:])+cos(r_sol[2,:]))
E_tot = T + V

plot(t,E_tot)
show()

# Generate animation of spheres
pxt1 = l*sin(r_sol[0,0])
pzt1 = l*cos(r_sol[0,0])
pxt2 = l*sin(r_sol[2,0])
pzt2 = l*cos(r_sol[2,0])
pxt1r = -pzt1
pzt1r = pxt1
pxt2r = -pzt2
pzt2r = pxt2
mass1 = sphere(pos=vector(pzt1r,pxt1r,0),radius=0.03)
mass2 = sphere(pos=vector(pzt1r+pzt2r,pxt1r+pxt2r,0),radius=0.03)
rod1 = cylinder(pos=vector(0,0,0),axis=vector(pzt1r,pxt1r,0),radius=0.005)
rod2 = cylinder(pos=vector(pzt1r,pxt1r,0),axis=vector(pzt2r,pxt2r,0),radius=0.005)
for tt in range(1,Nt):
    rate(200)
    th1 = r_sol[0,tt]
    pxt1 = l*sin(th1)
    pzt1 = l*cos(th1)
    th2 = r_sol[2,tt]
    pxt2 = l*sin(th2)
    pzt2 = l*cos(th2)

    pxt1r = -pzt1
    pzt1r = pxt1
    pxt2r = -pzt2
    pzt2r = pxt2
    mass1.pos=vector(pzt1r,pxt1r,0)
    rod1.axis=vector(pzt1r,pxt1r,0)
    rod2.pos=vector(pzt1r,pxt1r,0)
    mass2.pos=vector(pzt1r+pzt2r,pxt1r+pxt2r,0)
    rod2.axis=vector(pzt2r,pxt2r,0)
