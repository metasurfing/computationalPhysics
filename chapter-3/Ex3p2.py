# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:33:00 2020

@author: ljszym
"""

from math import pi
from pylab import plot,show
from numpy import linspace, sin, cos, exp

# (a)
theta = linspace(0,2*pi,100)

x = 2*cos(theta) + cos(2*theta)
y = 2*sin(theta) - sin(2*theta)

plot(x,y)
show()

# (b)

theta = linspace(0,10*pi,100)
r = theta**2

x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
show()

# (c)

theta = linspace(0,24*pi,1000)
r = exp(cos(theta)) - 2*cos(4*theta) + sin(theta/12)**5

x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
show()
