# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import plot,show
from numpy import linspace, loadtxt

def running_ave(Nspots,k,r):
    Yk = 0
    
    for rr in range(-r,r+1):
        if(k+rr>0 and k+r < len(Nspots)):
            Yk += 1/(2*r+1)*Nspots[k+rr]
    
    return Yk

r = 5
startPoint = 1
Npoints = 1000

data = loadtxt("../resources/sunspots.txt")
t = data[:,0]
Nspots = data[:,1]

N_run_ave = []

for kk in range(0,len(Nspots)):
    N_run_ave.append(running_ave(Nspots,kk,r))


plot(t[startPoint:(startPoint+Npoints)],Nspots[startPoint:(startPoint+Npoints)])
plot(t[startPoint:(startPoint+Npoints)],N_run_ave[startPoint:(startPoint+Npoints)])
show()