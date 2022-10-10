from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4

from numpy import sin, linspace, empty
from pylab import plot, xlabel, ylabel, show, legend

def f(x,t):
    return -x**3 + sin(t)

x0 = 0
t0 = 0
Ne = 500;
Nrk4 = 30
N = 100;
t = linspace(0,10,N)
te = linspace(0,10,Ne)
trk4 = linspace(0,10,Nrk4)
he = te[1]-te[0]
h = t[1]-t[0]
hrk4 = trk4[1] - trk4[0]

x_sol = empty(N,float)
x_sol[0] = x0

x_sol_rk4 = empty(Nrk4,float)
x_sol_rk4[0] = x0

x_sole = empty(Ne,float)
x_sole[0] = x0

for tt in range(1,Ne):
    x_sole[tt] = x_sole[tt-1] + he*f(x_sole[tt-1],te[tt-1])

for tt in range(1,N):
    k1 = h*f(x_sol[tt-1],t[tt-1])
    k2 = h*f(x_sol[tt-1]+0.5*k1,t[tt-1]+0.5*h)
    x_sol[tt] = x_sol[tt-1] + k2

# for tt in range(1,Nrk4):
#     k1 = hrk4*f(x_sol_rk4[tt-1],trk4[tt-1])
#     k2 = hrk4*f(x_sol_rk4[tt-1]+0.5*k1,trk4[tt-1]+0.5*hrk4)
#     k3 = hrk4*f(x_sol_rk4[tt-1]+0.5*k2,trk4[tt-1]+0.5*hrk4)
#     k4 = hrk4*f(x_sol_rk4[tt-1]+k3, trk4[tt-1]+hrk4)
#     x_sol_rk4[tt] = x_sol_rk4[tt-1] + 1/6*(k1 + 2*k2 + 2*k3 + k4)

x_sol_rk4 = rk4(f,trk4,t0,x0)
plot(t,x_sol)
plot(te,x_sole)
plot(trk4,x_sol_rk4)
xlabel('Time (sec)')
ylabel('x(t)')
legend(['RK2 {} pts'.format(N),'Euler {} pts'.format(Ne), 'RK4 {} pts'.format(Nrk4)], loc=3)
show()
