from numDiff import finiteDiff
from math import tanh, cosh
from numpy import linspace, zeros
from pylab import figure, plot, show, xlabel, ylabel

def f(x):
    return 1 + 0.5*tanh(2*x)

Np = 101
type = 'central'
x = linspace(-2,2,Np)
Dxf = zeros(Np)
Dxfa = zeros(Np)

for kk in range(Np):
    Dxf[kk] = finiteDiff(f,x[kk],0, type)
    Dxfa[kk] = 1/cosh(2*x[kk])**2

fig1 = figure(1)
plot(x,Dxfa)
plot(x,Dxf,':')
xlabel('x')
ylabel('Dxf')
show()
