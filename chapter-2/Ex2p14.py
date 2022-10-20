# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:21:40 2020

@author: ljszym
"""


def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)
    
M = 360
N = 0

print("The greatest common divisor of ", M, "and ", N, "is ", gcd(M,N))