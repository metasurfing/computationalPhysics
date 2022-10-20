# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:46:48 2020

@author: ljszym
"""


from vpython import sphere, rate, vector
from math import sin, cos, pi
from numpy import arange

s = sphere(pos=vector(1,0,0), radius = 0.1)

for theta in arange(0,10*pi,0.1):
    rate(30)
    x = cos(theta)
    y = sin(theta)
    s.pos = vector(x,y,0)