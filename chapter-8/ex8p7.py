from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from ode import rk4
from numpy import array, sqrt, empty, linspace, pi, sin, cos, zeros
from pylab import figure, xlabel, ylabel, plot, show, legend, ylim

m = 1
g = 9.81
C = 0.47
R = 0.08
rho = 1.22

for mm in range(1,6):
    m = mm
    def f(r,t):
        x1 = r[0]
        x2 = r[1]
        y1 = r[2]
        y2 = r[3]

        fx1 = x2
        fx2 = -1/2*pi*R**2*rho/m*C*sqrt(x2**2 + y2**2)*x2
        fy1 = y2
        fy2 = -g - 1/2*pi*R**2*rho/m*C*sqrt(x2**2 + y2**2)*y2
        return array([fx1, fx2, fy1, fy2],float)

    theta0 = 30/180*pi
    v0 = 100
    t0 = 0
    x0 = [0, v0*cos(theta0), 0, v0*sin(theta0)]
    t = linspace(0,10,1000)

    x_sol = rk4(f,t,x0,t0)

    plot(x_sol[0,:],x_sol[2,:])

ylim([0,150])
legend(['m = 1', 'm = 2', 'm = 3', 'm = 4', 'm = 5'])

show()

#As the mass increases, the distance traveled increases when the other properties are held constant
#This makes sense from the equations because the acceleration due to the drag
#terms are inversely proportional to mass when the air density and sphere radius are fixed.
#From the perspective of the physics it also makes sense because the cannonball has more
#momentum yet the rate at which it is transfering its momentum to the air is fixed by the
#surface area and density of the air.
