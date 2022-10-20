# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:26:31 2020

@author: ljszym
"""
#from numpy import array

def factorial(n):
    fact = 1;
    for ii in range(1,n+1):
        fact *= ii
    return fact


def binomial_coefficient(n,k):
    Cb = factorial(n)/(factorial(k)*factorial(n-k))
    return int(Cb)

def probability(n,k):
    
    p = binomial_coefficient(n,k)/2**n
    
    return p

#(a)
#print(binomial_coefficient(3,1))

#(b)
#Nlines = 20

#for n in range(1,Nlines+1):
#    currentRow = []
#    for k in range(0,n+1):
#        currentRow.append(binomial_coefficient(n, k))
#    print(array(currentRow,int))

#(c)

N = 100
N_heads = 49

print("Probability you get", N_heads, "heads: ", probability(N,N_heads))

P60orG = 1;

for kk in range(0, N_heads):
    P60orG -= probability(N,kk)
    
print("Probability you get atleast",N_heads,"heads: ", P60orG)