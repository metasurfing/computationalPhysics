# -*- coding: utf-8 -*-
"""
Spyder Editor

Dropping mass from height H
"""
import math

g_const = 9.81;

h = float(input("Enter the height of the tower: "))
t = math.sqrt(2*h/g_const)
print("The time to impact is", t,"seconds")
