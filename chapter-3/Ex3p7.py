# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:23:47 2020

@author: ljszym
"""

from pylab import imshow, show
from numpy import array, arange, empty, zeros,log10,ones

N = 1000
iterations = 100

c_R = empty([N,N],float)
c_I = empty([N,N],float)
c_plot = zeros([N,N],float)
c_plot_dB = ones([N,N],float)*iterations
count_R = 0
z = zeros([N,N], complex)

for rr in arange(-2,2, step = 4/N):
    count_I = 0
    for ii in arange(-2,2, step = 4/N):
        c_R[count_I,count_R] = rr
        c_I[count_I,count_R] = ii
        count_I += 1
    count_R +=1
    
c = c_R + 1j*c_I

'''
for nn in range(iterations):
    z = z**2 + c
    

for ii in range(N):
    for jj in range(N):
        if(abs(z[ii,jj])<2):
            c_plot[ii,jj] = 0
        else:
            c_plot[ii,jj] = 1
'''

for nn in range(iterations):
    z = z**2 + c  
    Mz = array(list(map(abs,z)),float)
    c_plot[Mz>2] = nn+1
    c_plot_dB[Mz>2] = log10(nn+1)


    
imshow(c_plot)
show()
   
imshow(c_plot_dB)
show()     
        
        
