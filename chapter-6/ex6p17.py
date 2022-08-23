from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from nlsolve import newton_method
from numpy import array, exp, empty, zeros

Vt = 0.05
Vp = 5
I0 = 3e-9
R1 = 1e3
R2 = 4e3
R3 = 3e3
R4 = 2e3
def func(x):
    f = empty(2,float)
    f[0] = x[0]*(1/R1 + 1/R2) + I0*exp((x[0]-x[1])/Vt) - I0 - Vp/R1
    f[1] = x[1]*(1/R3 + 1/R4) - I0*exp((x[0]-x[1])/Vt) - I0 - Vp/R3
    return f

def jacobian(x):
    grad = zeros([2, 2], float)
    grad[0,0] = 1/R1 + 1/R2 + I0/Vt*exp((x[0]-x[1])/Vt)
    grad[0,1] = -I0/Vt*exp((x[0]-x[1])/Vt)
    grad[1,0] = -I0/Vt*exp((x[0]-x[1])/Vt)
    grad[1,1] = 1/R3 + 1/R4 + I0/Vt*exp((x[0]-x[1])/Vt)
    return grad

v0 = zeros(2)
v = newton_method(func,v0, grad = jacobian)
print(v[0]-v[1])
