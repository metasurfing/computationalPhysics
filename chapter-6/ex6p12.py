from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from nlsolve import relaxationNd
from numpy import empty, sqrt
a = 1
b = 2
def func(x):
    fout = empty(len(x),float)
    fout[0] = x[1]*(a+x[0]**2)
    fout[1] = b/(a+x[0]**2)
    return fout

x0 = empty(2,float)
x0[0] = 1
x0[1] = 1
xsol, iter = relaxationNd(func,x0, count = 1, maxIter = 40)

print(xsol)
print(iter)

def func1(x):
    fout = empty(len(x),float)
    fout[0] = sqrt(b/x[1] - a)
    fout[1] = x[0]/(a+x[0]**2)
    return fout

x0 = empty(2,float)
x0[0] = 1
x0[1] = 1
xsol, iter = relaxationNd(func1,x0,tol = 1e-8,count = 1, maxIter = 40)

print(xsol)
print(iter)
print(func1(xsol))
