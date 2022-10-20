# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:42:48 2020

@author: ljszym
"""
from math import sqrt, atan2, pi

x = float(input("Please provide the current 'x' coordinate: "))
y = float(input("Please provide the current 'y' coordinate: "))

r = round(sqrt(x**2+y**2),2)
theta = round(atan2(y,x),2)

print("The polar coordinates are: r = ",r,"theta = ", theta*180/pi,"degrees")
