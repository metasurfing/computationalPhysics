from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4

from numpy import sin, linspace, empty, transpose
from pylab import plot, xlabel, ylabel, show, legend, xlim

def f(x,u):
    return 1/(x**2 * (1-u)**2 + u**2)

x0 = 1.0
u0 = 0.0
N = 100


upoints = linspace(0,0.99,N)
h = upoints[1] - upoints[0]

x_sol = empty([1,N],float)

# for tt in range(1,Nrk4):
#     k1 = hrk4*f(x_sol_rk4[tt-1],trk4[tt-1])
#     k2 = hrk4*f(x_sol_rk4[tt-1]+0.5*k1,trk4[tt-1]+0.5*hrk4)
#     k3 = hrk4*f(x_sol_rk4[tt-1]+0.5*k2,trk4[tt-1]+0.5*hrk4)
#     k4 = hrk4*f(x_sol_rk4[tt-1]+k3, trk4[tt-1]+hrk4)
#     x_sol_rk4[tt] = x_sol_rk4[tt-1] + 1/6*(k1 + 2*k2 + 2*k3 + k4)

x_sol = rk4(f,upoints,x0,u0)
t = upoints/(1-upoints)
plot(t,transpose(x_sol))
xlabel('Time (sec)')
ylabel('x(t)')
xlim([0, 80])
show()
