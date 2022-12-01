from random import random
from numpy import arange
from pylab import plot,show,xlabel,ylabel,legend


Ntl = 1000
Npb = 0
h = 1
tmax = 1000
Tau = 3.053*60
tpoints = arange(0,tmax,h)
Ntl_points = []
Npb_points = []
p = 1-2**(-h/Tau)

for tt in tpoints:
    decay = 0
    for kk in range(Ntl):
        if random() < p:
            decay += 1
    Ntl -= decay
    Npb += decay
    Ntl_points.append(Ntl)
    Npb_points.append(Npb)

plot(tpoints/60,Ntl_points)
plot(tpoints/60,Npb_points)
xlabel('Time (min)')
ylabel('Number of atoms')
legend(['Tl','Pb'])
show()
