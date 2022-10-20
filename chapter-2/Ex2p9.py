# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:56:11 2020

@author: ljszym
"""
from math import sqrt

L = 100
M = 0.0

for ii in range(-L,L+1):
    for jj in range(-L,L+1):
        for kk in range(-L,L+1):
            if(ii == 0 and jj == 0 and kk == 0):
                continue
            elif((ii+jj+kk)%2 == 0):
                M += 1/sqrt(ii**2 + jj**2 + kk**2)
            else:
                M -= 1/sqrt(ii**2 + jj**2 + kk**2)
                
print("The Madelung constant with L = ", L, "is ", M)
                