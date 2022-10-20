# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:33:19 2020

@author: ljszym
"""

from numpy import array, loadtxt
from pylab import plot, show

data = loadtxt("../resources/millikan.txt",float)

e_charge = 1.602*10**-19
h_true = 6.62607015*10**-34

x = data[:,0]
y = data[:,1]
N = len(x)

Ex = sum(x)/N
Ey = sum(y)/N
Exx = sum(x**2)/N
Exy = sum(x*y)/N

m = (Exy-Ex*Ey)/(Exx-Ex**2)
c = (Exx*Ey-Ex*Exy)/(Exx-Ex**2)
print("The slope is: m = ",m, "The y-intercept is: c = ", c)

h = m*e_charge
print("The calculated value for Planck's constant is h = ", h)
print("The true value of Planck's constant is h = ", h_true)
print("The percent error in h is: ", (h-h_true)/h_true*100)

y_fitted = m*x+c

plot(x,y, "k.")
plot(x,y_fitted, "k-")
show()
