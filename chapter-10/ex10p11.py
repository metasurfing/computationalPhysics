from vpython import sphere, vector, curve, rate
from numpy import zeros, exp, sum
from random import random, randrange
from pylab import imshow,show,draw,plot,figure

N = 50
Tmax = 10
Tmin = 1e-3

grid = zeros([N,N],int)
t = 0
tau = 10000
T = Tmax
dimers = []
energy = []

while T >= Tmin:

    T = Tmax*exp(-t/tau)
    t += 1

    idx11 = randrange(N)
    idx21 = randrange(N)
    idx22 = idx21
    idx12 = idx11

    while (idx22 == idx21 and idx11 == idx12) or idx12 < 0 or idx22 < 0 or idx12 > 49 or idx22 > 49:
        if random()<=0.5:
            if random() <= 0.5:
                idx12 = idx11 + 1
            else:
                idx12 = idx11 - 1
        else:
            if random() <= 0.5:
                idx22 = idx21 + 1
            else:
                idx22 = idx21 - 1

    #Current dimer
    dimer_cur = [[idx11,idx21],[idx12, idx22]]

    #Current enery
    Ecur = -len(dimers)
    dE = 1

    if dimers.count(dimer_cur):
        if random() < exp(-dE/T):
            dimers.remove(dimer_cur)
            grid[idx11,idx21] = 0
            grid[idx12,idx22] = 0
    elif grid[idx11,idx21] + grid[idx12,idx22] == 0:
        grid[idx11,idx21] = 1
        grid[idx12,idx22] = 1
        dimers.append(dimer_cur)

    energy.append(-len(dimers))

figure(1)
plot(energy)
figure(2)
imshow(grid)
show()
