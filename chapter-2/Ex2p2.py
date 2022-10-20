# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:43:30 2020

@author: ljszym

a) Fc = M_satellite*v^2/R
   Fg = G*M_earth*M_satellite/R^2
   T = 2*pi*(R_earth+R)/v
   
   force balance gives the desired result of R = (G*M_earth*T^2/(4*pi^2))^(1/3) - R_earth
"""

G = 6.67*10**-11
M_earth = 5.96*10**24
R_earth = 6371*10**3
pi = 3.14159265358979
T = float(input("Please provide the desired orbital period T in seconds:"))

h = (G*M_earth*T**2/(4*pi**2))**(1/3)-R_earth

print("The required height above Earth's surface is",h,"meters")

