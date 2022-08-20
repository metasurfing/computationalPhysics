from numpy import tanh, cosh, linspace, ones, amax
from pylab import plot, show, ylim, xlabel, ylabel

Tmax = 2.0
accuracy = 1e-6
npoints = 1001

y = []
temp = linspace(0.01,Tmax,npoints)

m1 = ones(npoints,float)
error = ones(npoints,float)

while amax(abs(error)>accuracy):
    m1, m2 = tanh(m1/temp), m1
    error = abs((m1-m2)/(1-temp*cosh(m2/temp)**2))

plot(temp,m1)
ylim(-0.1,1.1)
xlabel('Temperature')
ylabel('Magnetization')
show()
