from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from ode import rk4
from numpy import linspace, empty, floor
from pylab import plot, xlabel, ylabel, legend, ylim, xlim, show

def Vin(x):
    if floor(2*x)%2 == 0:
        return 1.0
    else:
        return -1.0


t0 = 0
V0 = 0
tf = 10
N = 2000
RC = [0.01, 0.1, 1]
t = linspace(t0,tf,N)
Vsol = empty([len(RC), N])

for jj in range(0,len(RC)):
    def f(Vout,T):
        return 1/RC[jj] * (Vin(T) - Vout)
    Vsol[jj,:] = rk4(f,t,V0,t0)

plot(t,Vsol[0,:])
plot(t,Vsol[1,:])
plot(t,Vsol[2,:])

legend(['RC = 0.01','RC = 0.1', 'RC = 1'])
ylim([-1.5, 1.5])
xlim([0, 2])
show()

#The larger the RC constant the slower the capacitor charges for each cycle producing
#different rise times for each graph. With RC = 0.01 the capacitor quickly charges and
#discharges during each half second +1 and -1 cycle, with RC = 0.1 the capacitor fully
#charges but significanly slower during each half cycle, and with RC = 1 the capacitor
#doesn't charge fully as the time constant is longer than the length of time the input
#voltage is high or low. This can also be interpreted in terms of the cut off frequency of
#the low-pass filter where the corner frequency is 1/RC. When RC is small more high frequency
#content is retained allowing for shorter rise times and when RC is larger more of the
#high frequency content is attenuated and the rise times are longer.
