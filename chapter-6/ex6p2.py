import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from linearAlg import gaussElim
from numpy import array
from numpy.linalg import solve

A = array([[2, 1, 4, 1],
          [3, 4, -1, -1],
          [1, -4, 1, 5],
          [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
x = gaussElim(A,v)

print(x)


A = array([[0, 1, 4, 1],
            [3, 4, -1, -1],
            [1, -4, 1, 5],
            [2, -2, 1, 3]],float)
v = array([-4, 3, 9, 7],float)

x = gaussElim(A,v)
x_linalg = solve(A,v)

print(x)
print(x_linalg)
