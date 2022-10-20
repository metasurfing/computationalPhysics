# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:58:17 2020

@author: ljszym
"""
from math import sqrt


x = float(input("Provide a distance of travel in light years: "))
v = float(input("Provide the velocity relative to the speed of light: "))

t_ship = x/v;
t_earth = t_ship/sqrt(1-v**2)

print("The time on the ship is:", t_ship, "years.")
print("The time on Earth is:", t_earth, "years.")