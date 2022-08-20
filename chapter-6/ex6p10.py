from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from nlsolve import relaxationNd
from numpy import exp, empty, arange
from pylab import plot, show, xlabel, ylabel

c = 2

def func(x):
    return 1-exp(-c*x)

Nvars = 1
x0 = empty(Nvars,float)
for kk in range(Nvars):
    x0[kk] = 1

xsol = relaxationNd(func,x0,tol = 1e-6)

print(xsol)
print(func(xsol))

cr = arange(0,3,0.01)
x_sol = empty(len(cr))

for kk in range(len(cr)):
    c_cur = cr[kk]
    def func(x):
        return 1-exp(-c_cur*x)

    x_sol[kk] = relaxationNd(func,x0,tol=1e-6)

plot(cr,x_sol)
xlabel('Decay rate')
ylabel('x-solution')
show()
