# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:05:59 2020

@author: ljszym
"""
def factorial(N):
    if(N==1):
        return 1
    else:
        return N*factorial(N-1)
    
N = 200

print(factorial(N)//10**374)

'''
Answer to question:
    
    It works with the integer because integers can take on arbitrarily large values.
    Since the number is on the order 10^374 it overflows as a floating point number.

'''
    

