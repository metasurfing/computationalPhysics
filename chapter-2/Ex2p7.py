# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:28:46 2020
Catalan numbers up to 1 billion
@author: ljszym
"""

C0 = 1
Cn = C0;
n = 0;
while(Cn<=10**9):
    print(Cn)
    Cn = int((4*n+2)/(n+2)*Cn)
    n += 1
    