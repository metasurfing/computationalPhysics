from random import random
from math import cos, pi, exp, sqrt, log
from pylab import plot, show
# def f(x):
#     return x**2 - cos(4*pi*x)
def f(x):
    return cos(x) + cos(sqrt(2)*x) + cos(sqrt(3)*x)
Tmax = 1
Tmin= 1e-4

steps = 1000
t = 0
Tau = 100
x = 25
xpoints = []
T = Tmax
sigma = 25

while T > Tmin:

    T = Tmax*exp(-t/Tau)

    delta = sqrt(-2*sigma**2*log(1-random()))*cos(2*pi*random())
    xnew = x + delta
    while xnew > 50 or xnew < 0:
        delta = sqrt(-2*sigma**2*log(1-random()))*cos(2*pi*random())
        xnew = x + delta

    fcur = f(x)
    fnew = f(xnew)
    dF = fnew - fcur

    if random() < exp(-dF/T):
        x = xnew

    t += 1
    xpoints.append(x)

print(x)
plot(xpoints,'.')
show()
