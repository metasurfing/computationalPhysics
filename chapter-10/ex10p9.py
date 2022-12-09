from vpython import sphere, vector, color, rate
from random import random, randrange
from numpy import ones, sum, exp, empty
from pylab import plot, ylabel, show
J = 1
N = 20
T = 3
kB = 1
# steps = 1000000
steps = 1000000
def Energy(spins):
    return -J*(sum(spins[0:(N-1),:]*spins[1:N,:])+sum(spins[:,0:(N-1)]*spins[:,1:N]))

Mplot = []

magnet = ones([N,N],int)
particles = empty([N,N],sphere)

for jj in range(N):
    for ii in range(N):
        # particles[ii,jj] = sphere(pos = vector(ii-N/2,jj-N/2,0), radius = 0.3, color = color.blue)
        if random() < 0.5:
            magnet[ii,jj] = -1
            # particles[ii,jj].color = color.red



for nn in range(steps):
    magnet_new = magnet.copy()
    idx1 = randrange(N)
    idx2 = randrange(N)

    magnet_new[idx1,idx2] = -1*magnet_new[idx1,idx2]

    Enew = Energy(magnet_new)
    Eold = Energy(magnet)

    dE = Enew-Eold

    if random()<exp(-dE/(kB*T)):
        magnet = magnet_new.copy()

    # rate(10000)
    # if magnet[idx1,idx2]>0:
    #     particles[idx1,idx2].color = color.blue
    # else:
    #     particles[idx1,idx2].color = color.red

    Mplot.append(sum(magnet))


plot(Mplot)
show()

#Part C:
#The magnetization is sometimes negative and sometimes positive.
#Since the magnetization starts at approximately zero and the choice of whether or
#not the changes in magnetization flips to positive or negative is random, either the
#positive or negative magnetization can lower the total energy and become the dominant direction

#Part D:
#As the temperature increases the magnitude of the total magnetization decreases.
#This is because as the temperature increases it becomes more likely that transitions to
#states that increase the total energy of the system occur. Therefore neither magnetization
#becomes dominant because it becomes more probable that two magnetizations of opposite
#sign will be next to each other.
