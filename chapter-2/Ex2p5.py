# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:50:30 2020

@author: ljszym
"""

from math import sqrt, pi

Me = 9.11*10**-13
Ee = 10
Eb = 9
h_bar = 6.626*10**-34/2/pi

k1 = sqrt(2*Me*Ee)/h_bar
k2 = sqrt(2*Me*(Ee-Eb))/h_bar

T= 4*k1*k2/(k1+k2)**2
R = (k1-k2)**2/(k1+k2)**2

print("The probability the electron is: Transmitted ", T, " Reflected ", R)