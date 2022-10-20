# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:44:03 2021

@author: ljszym
"""

from math import  pi
from numpy import arange,empty,sin, cos, sqrt, zeros,newaxis
from pylab import plot, imshow, show


'''
Part (a)
'''
def f(x,m,theta):
    return cos(m*theta-x*sin(theta))

def J(m,x):
    a = 0
    b = pi
    N = 1000
    h = (b-a)/N
    
    s = f(x,m,a)+f(x,m,b)
    
    for kk in range(1,N,2):
        s += 4*f(x,m,a+kk*h)
    
    for kk in range(2,N,2):
        s += 2*f(x,m,a+kk*h)
        
    return 1/pi*s*h/3

x1 = 0
x2 = 20
dx = 0.1
M = 3

x = list(arange(x1,x2+dx,dx))
Jmx = empty([len(x),M],float)

for mm in range(0,M):
    for nn in range(0,len(x)):
        Jmx[nn,mm] = J(mm,nn*dx)
    plot(x,Jmx[:,mm])
    
show()

'''
Part (b)
'''

N = 600
xmax = 10**-6
ymax = 10**-6
dx = xmax/N
dy = ymax/N

lambda0 = 500*10**-9
k = 2*pi/lambda0
R = empty([2*N+1, 2*N+1], float)
J2d = empty([2*N+1, 2*N+1], float)

xx = arange(-xmax,xmax+dx,dx) + zeros([2*N+1,1],float)
yy = zeros([1,2*N+1],float)+ arange(-ymax,ymax+dy,dy)[:, newaxis]

R = sqrt(xx**2+yy**2)
J2d = J(1,k*R)/(k*R)
J2d[R==0] = 1/2

        
imshow(J2d**2,vmax = 0.01)        
