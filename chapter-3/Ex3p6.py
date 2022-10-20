# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:43:36 2020

@author: ljszym
"""

from pylab import scatter, plot, show
from numpy import array, arange, ones, shape

N = 1000
'''
#This is absurbdly slowwwwwwww

for rr in arange(1,4,0.01):
    x = 1/2
    for nn in range(N):
        x = rr*x*(1-x)
    for nn in range(N):
        x = rr*x*(1-x)
        scatter(rr,x)
        
show()
'''

r = array(list(arange(1,4,0.01)),float)
x = ones(shape(r),float)*1/2

for nn in range(N):
    x = r*x*(1-x)
    
for nn in range(N):
    x = r*x*(1-x)
    scatter(r,x)

show()
