from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from ode import rk4

from numpy import empty, array, linspace
from pylab import plot, legend, show, xlabel, ylabel

a = 1
b = 0.5
g = 0.4
d = 2

def f(r,t):
    x = r[0]
    y = r[1]

    fx = a*x - b*x*y
    fy = g*x*y - d*y

    return array([fx, fy], float)

t0 = 0
x0 = array([2, 2], float)
t = linspace(0,30, 1000)

pop = rk4(f,t,x0,t0)

plot(t,pop[0,:])
plot(t,pop[1,:])
legend(['rabbits','foxes'])
xlabel('Time')
ylabel("Population (in 1000's)")
show()

#The populations start off at an equal value, but since the foxes die (d) at a faster
#rate than the rabbits are born (a) the population of the foxes initially decreases.
#This allows for the rabbit population to initially grow. However, once the rabbit population
#becomes sufficiently large the population of the foxes starts to out pace their death rate.
#Which then increases the death rate of rabbits eventually causing a decrease. This in turn
#reduces the growth rate of the foxes until we get back to the intial condition and then
#the process repeats.
