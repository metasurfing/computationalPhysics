from numpy import sin, linspace, empty
from pylab import plot, xlabel, ylabel, show, legend

def f(x,t):
    return -x**3 + sin(t)

x0 = 0
t0 = 0
Ne = 500;
N = 100;
t = linspace(0,10,N)
te = linspace(0,10,Ne)
he = te[1]-te[0]
h = t[1]-t[0]

x_sol = empty(N,float)
x_sol[0] = x0

x_sole = empty(Ne,float)
x_sole[0] = x0

for tt in range(1,Ne):
    x_sole[tt] = x_sole[tt-1] + he*f(x_sole[tt-1],te[tt-1])

for tt in range(1,N):
    k1 = h*f(x_sol[tt-1],t[tt-1])
    k2 = h*f(x_sol[tt-1]+0.5*k1,t[tt-1]+0.5*h)
    x_sol[tt] = x_sol[tt-1] + k2

plot(t,x_sol)
plot(te,x_sole)
xlabel('Time (sec)')
ylabel('x(t)')
legend(['Runge-Kutta (2nd) {} pts'.format(N),'Euler {} pts'.format(Ne)], loc=3)
show()
