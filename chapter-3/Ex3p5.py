# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:19:53 2020

@author: ljszym
"""


from vpython import sphere, rate, vector, color, canvas
from numpy import empty, arange
from math import sin, cos, pi

N_planets = 6
c1 = 700
c2 = 1
c_sun = 300

R_sun = c_sun*695500

R_mercury = c1*2440
R_mercury_orbit = 57.9*10**6 + R_sun
T_mercury = 88

R_venus = c1*6052
R_venus_orbit = 108.2*10**6 + R_sun
T_venus = 224.7

R_earth = c1*6371
R_earth_orbit = 149.6*10**6 + R_sun
T_earth = 365.3

R_mars = c1*3386
R_mars_orbit = 227.9*10**6 + R_sun
T_mars = 687

R_jupiter = c1*69173
R_jupiter_orbit = 778.5*10**6 + R_sun
T_jupiter = 4331.6

R_saturn = c1*57316
R_saturn_orbit = 1433.4*10**6 + R_sun
T_saturn = 10759.2



R_Planets = [R_mercury, R_venus, R_earth, R_mars, R_jupiter, R_saturn]
R_orbit= [R_mercury_orbit, R_venus_orbit, R_earth_orbit, R_mars_orbit, R_jupiter_orbit, R_saturn_orbit]
T_Planets = [T_mercury, T_venus, T_earth, T_mars, T_jupiter, T_saturn]

Planets = empty(N_planets+1,sphere)

canvas(width = 1900, height = 900)
sphere(radius = R_sun, pos = vector(0,0,0), color=color.yellow)

for jj in range(0,N_planets):
    Planets[jj] = sphere(radius = R_Planets[jj], pos = vector(R_orbit[jj],0,0))

Planets[0].color = color.magenta
Planets[1].color = color.green
Planets[2].color = color.blue
Planets[3].color = color.red
Planets[4].color = color.cyan
Planets[5].color = color.white


for tt in arange(0,1*max(T_Planets),c2):
    rate(30)
    for jj in range(0,N_planets):
        Planets[jj].pos = vector(R_orbit[jj]*cos(tt/T_Planets[jj]*2*pi),R_orbit[jj]*sin(tt/T_Planets[jj]*2*pi),0)


