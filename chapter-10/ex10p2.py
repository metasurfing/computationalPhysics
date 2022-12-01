from random import random
from numpy import arange
from pylab import plot,show,xlabel,ylabel,legend

#Atoms of each isotope
Nbi_213 = 10000
Nbi_209 = 0
Ntl = 0
Npb = 0

#Half-life of each isotope
Tau_tl = 2.2*60
Tau_pb = 3.3*60
Tau_bi213 = 46*60

#Time step
h = 1

#Final time
tmax = 20000

#Time steps
tpoints = arange(0,tmax,h)

#Probability of decay
p_pb = 1-2**(-h/Tau_pb)
p_tl = 1-2**(-h/Tau_tl)
p_bi213 = 1-2**(-h/Tau_bi213)

#Number of each isotope at current time step
Ntl_points = []
Npb_points = []
Nbi213_points = []
Nbi209_points = []
total_points = []

for tt in tpoints:
    decay_pb = 0
    decay_tl = 0
    decay_bi213pb = 0
    decay_bi213tl = 0

    for kk in range(Npb):
        if random() < p_pb:
            decay_pb += 1

    for kk in range(Ntl):
        if random() < p_tl:
            decay_tl += 1

    Ntl -= decay_tl
    Npb -= decay_pb
    Nbi_209 += (decay_tl + decay_pb)

    for kk in range(Nbi_213):
        if random() < p_bi213:
            if random() < 0.9791:
                decay_bi213pb += 1
            else:
                decay_bi213tl += 1
    Ntl += decay_bi213tl
    Npb += decay_bi213pb
    Nbi_213 -= (decay_bi213pb + decay_bi213tl)

    Ntl_points.append(Ntl)
    Npb_points.append(Npb)
    Nbi209_points.append(Nbi_209)
    Nbi213_points.append(Nbi_213)
    total_points.append(Ntl+Npb+Nbi_209+Nbi_213)

plot(tpoints/60,Ntl_points)
plot(tpoints/60,Npb_points)
plot(tpoints/60,Nbi209_points)
plot(tpoints/60,Nbi213_points)
plot(tpoints/60,total_points)
xlabel('Time (min)')
ylabel('Number of atoms')
legend(['Tl','Pb','Bi209','Bi213', 'Total # of atoms'])
show()
