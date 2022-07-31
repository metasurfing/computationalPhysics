import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from numInt import trapInt1D, eulerMaclaurin1D

def f(x):
    return x**4 - 2*x + 1

a = 0
b = 2
N = 10

s_trap = trapInt1D(f,a,b,N,opt = 'Romberg')
s_em = eulerMaclaurin1D(f,a,b,N)

print(s_trap)
print(s_em)

#This integration technique is very accurate for smooth functions
#However, I would expect it to perform very poorly on noisy data or nonsmooth functions.
#For this reason I don't expect it to be used in practice very often.
