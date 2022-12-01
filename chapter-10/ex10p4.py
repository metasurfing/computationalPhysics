from numpy import zeros, log, arange, sort, shape
from random import random
from pylab import plot, show, xlabel, ylabel

N = 1000
tau = 3.053*60
times = zeros(N,float)


def t(z):
    return -tau/log(2)*log(1-z)

for jj in range(0,N):
    times[jj] = t(random())

times = sort(times)
t_axis = arange(0,N,1/2)
atoms = zeros(2*N,float)

decayed = 0
for tt in range(0,2*N):
    for jj in range(decayed,N):
        if times[jj]<=t_axis[tt]:
            decayed += 1
    atoms[tt] = N - decayed

plot(t_axis/60,atoms)
xlabel('time (min.)')
ylabel('Number of atoms')
show()
