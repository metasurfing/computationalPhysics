# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:19:53 2020

@author: ljszym
"""

from pylab import imshow, show, gray
from numpy import loadtxt

data = loadtxt("../resources/stm.txt")

imshow(data, origin='lower',extent = [0,1,0,1])
gray()
show()
