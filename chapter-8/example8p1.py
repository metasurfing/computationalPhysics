from numpy import sin, linspace, empty
from pylab import plot, xlabel, ylabel, show

def f(x,t):
    return -x**3 + sin(t)

x0 = 0
t0 = 0
N = 10;
t = linspace(0,10,N)
h = t[1]-t[0]

x_sol = empty(N,float)
x_sol[0] = x0

for tt in range(1,N):
    x_sol[tt] = x_sol[tt-1] + h*f(x_sol[tt-1],t[tt-1])

plot(t,x_sol)
xlabel('Time (sec)')
ylabel('x(t)')
show()
