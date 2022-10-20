# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:13:24 2020

@author: ljszym
"""

def Catalan_numbers(n):
    if n == 0:
        return 1
    else:
        return (4*n-2)/(n+1)*Catalan_numbers(n-1)

N = 6
print("The ", N, "th Catalan number is: ", int(Catalan_numbers(N)))
