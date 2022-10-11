from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4

from numpy import sin, linspace, empty, transpose, array
from pylab import plot, xlabel, ylabel, show, legend, xlim

def f(r,t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + sin(t)**2
    return array([fx, fy],float)

a = 0.0
b = 10.0
N = 1000
t = linspace(a,b,N)
x0 = array([1, 1], float)
t0 = 0
# for tt in range(1,Nrk4):
#     k1 = hrk4*f(x_sol_rk4[tt-1],trk4[tt-1])
#     k2 = hrk4*f(x_sol_rk4[tt-1]+0.5*k1,trk4[tt-1]+0.5*hrk4)
#     k3 = hrk4*f(x_sol_rk4[tt-1]+0.5*k2,trk4[tt-1]+0.5*hrk4)
#     k4 = hrk4*f(x_sol_rk4[tt-1]+k3, trk4[tt-1]+hrk4)
#     x_sol_rk4[tt] = x_sol_rk4[tt-1] + 1/6*(k1 + 2*k2 + 2*k3 + k4)

x_sol = rk4(f,t,x0,t0)
plot(t,transpose(x_sol[0,:]))
plot(t,transpose(x_sol[1,:]))
xlabel('Time (sec)')
ylabel('x(t), y(t)')
legend(['x','y'])
show()
