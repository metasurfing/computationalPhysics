# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:19:29 2020

@author: ljszym
"""
from math import pi, sqrt

M = 1.9891*10**30
G = 6.6738*10**-11

v1 = float(input("Please provide the velocity at perihelion: "))
l1 = float(input("Please provide the distance to the sun at perihelion: "))

v2 = min(v1,2*G*M/(l1*v1)-v1)
l2 = l1*v1/v2

a = 1/2*(l1+l2)
b = sqrt(l1*l2)
T = 2*pi*a*b/(l1*v1)
eccentricity = (l2-l1)/(l1+l2)

sec_hour = 60*60
sec_year = 60*60*24*365

print("aphelion l2 = ", l2, "v2 = ",v2)

if(T>sec_year):
    print("Period T = ", T/sec_year, "years")
else:
    print("Period T = ", T/sec_hour, "hours")

print("Eccentricity: ", eccentricity)