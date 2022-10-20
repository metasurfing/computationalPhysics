# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:24:32 2020

@author: ljszym
"""
from math import sqrt

a, b, c = map(float,input("Provide the coefficients a, b, c in ax^2+bx+c = 0: ").split())

x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print("The positive root is: ", x1, "The negative root is: ", x2)
print("The equation is for + is: ", a*x1**2+b*x1+c)
print("The equation is for - is: ", a*x2**2+b*x2+c)

x1_alt = 2*c/(-b - sqrt(b**2 - 4*a*c))
x2_alt = 2*c/(-b + sqrt(b**2 - 4*a*c))

print("The positive root is: ", x1_alt, "The negative root is: ", x2_alt)
print("The equation is for + is: ", a*x1_alt**2+b*x1_alt+c)
print("The equation is for - is: ", a*x2_alt**2+b*x2_alt+c)



x1_new = 2*c/(-b - sqrt(b**2 - 4*a*c))
x2_new = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print("The positive root is: ", x1_new, "The negative root is: ", x2_new)
print("The equation is for + is: ", a*x1_new**2+b*x1_new+c)
print("The equation is for - is: ", a*x2_new**2+b*x2_new+c)
    