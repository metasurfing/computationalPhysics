# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from vpython import sphere, vector, color

L = 5
R_Na = 0.4
R_Cl = 0.6
R = 0.2

#NaCl Lattice
for i in range(-L,L+1):
    for j in range(-L,L+1):
      for k in range(-L,L+1):
          if((i+j+k)%2 == 0):
              sphere(radius = R_Na, pos=vector(i, j, k))
          else:
              sphere(radius = R_Cl, pos=vector(i, j, k), color = color.blue)

#FCC lattice
'''
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            sphere(radius = R, pos=vector(i, j, k))
            
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L+1):
            sphere(radius = R, pos=vector(i+0.5, j+0.5, k))
            
for i in range(-L,L):
    for j in range(-L,L+1):
        for k in range(-L,L):            
            sphere(radius = R, pos=vector(i+0.5, j, k+0.5))
           
for i in range(-L,L+1):
    for j in range(-L,L):
        for k in range(-L,L):               
            sphere(radius = R, pos=vector(i, j+0.5, k+0.5))
'''