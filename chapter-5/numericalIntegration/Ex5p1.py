# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:52:11 2021

@author: ljszym
"""

from pylab import plot, show
from numpy import loadtxt, empty

data = loadtxt('../resources/velocities.txt', float)

s = 0
#s = 1/2*(data[0,1]+data[-1,1])
dt = data[1,0]-data[0,0]
distance_time = empty([len(data),1],float)
distance_time[0,0] = 0

for kk in range(1,len(data)-1):
    
    if kk == 1:
        s = 1/2*(data[0,1])*dt
        print(s)
    s += data[kk,1]
    distance_time[kk,0] = s*dt
    
    if kk == (len(data)-2):
        s += 1/2*data[-1,1]*dt
        distance_time[kk+1,0] = s
        print(s)

I = s*dt

plot(data[:,0],data[:,1])
plot(data[:,0], distance_time)
show()