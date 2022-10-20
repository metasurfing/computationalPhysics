# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:17:42 2020

@author: ljszym
"""
from numpy import inf, arange

#A = float(input("Input the mass number (A): "))
#Z = float (input("Input the atomic number (Z): "))

a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2
Amin = [];
B_pN_min = [];
B_pn_max =  -inf

for Z in range(1,101):
    B_pN_m = inf
    for A in arange(Z,3*Z+1):
    
        if(A%2 != 0):
            a5 = 0.0
        elif(A%2==0 and Z%2 == 0):
            a5 = 12.0
        else:
            a5 = -12.0    
    
        B = a1*A - a2*A**(2/3) - a3*Z**2/A**(1/3) - a4*(A-2*Z)**2/A + a5/A**(1/2)
        B_per_nucleon = B/A
    
        if(B_per_nucleon < B_pN_m):
            
            B_pN_m = B_per_nucleon
            B_pN_min.append(B_per_nucleon)
            Amin.append(A)

for Z in range(0,100):
    if(B_pN_min[Z]>B_pn_max):
        B_pn_max = B_pN_min[Z]
        Z_max = Z+1
                
                  
print("The minimizing mass numbers are: ",Amin)
print("The atomic number with the maximum binding energy per nucleon is: ", Z_max)
        
    
    


#print("The binding energy is: ",B)
#print("The binding energy per nucleon is: ", B/A)