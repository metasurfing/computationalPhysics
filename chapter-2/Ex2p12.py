# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:01:49 2020

@author: ljszym
"""
from math import sqrt

def check_primeness(N,primes):
    sN = sqrt(N)
    
    for kk in primes:
        if(kk>sN):
            primes.append(N)
            break
        if(N%kk == 0):
            break
        
    return primes

N = 10000
primes = [2]

for nn in range(3,N+1):
    primes = check_primeness(nn,primes)
    
print("The prime numbers up to ", N, "are: ", primes)