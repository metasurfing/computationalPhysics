import numInt as ni
from cv import cv
from pylab import plot, show, xlabel, ylabel, figure


rho = 6.022*10**28 #number density of solid Al in 1/m^3
ThetaD = 428 #Debye temperature of Al in K
Vcc = 1000 #Volume in cubic cm
V = Vcc/100/100/100
N = 50 #number of sample points
kB = 1.380649*10**-23
T =  list(range(5, 500, 5))
x, w = ni.gaussxw(N)
a = 0
Cv = [0]*len(T)
Cvn = [0]*len(T)

for kk in range(len(T)):
    b = ThetaD/T[kk]
    xk = 0.5*b*x + 0.5*b
    wk = 0.5*b*w
    Cv[kk] = cv(T[kk],ThetaD,V,rho,N,xk,wk)
    Cvn[kk] = cv(T[kk],ThetaD,V,rho,N,xk,wk)/(3*rho*V*kB)

f1 = figure(1)
plot(T,Cvn)
xlabel('T')
ylabel('Normalized Heat Capacity ')


f2 = figure(2)
plot(T,Cv)
xlabel('T')
ylabel('Heat Capacity (J/K)')

show()
