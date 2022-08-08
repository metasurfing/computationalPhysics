import sys
sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')

from linearAlg import gaussElim
from numpy import array, dot

# A = array([[2, 1, 4, 1],
#           [3, 4, -1, -1],
#           [1, -4, 1, 5],
#           [2, -2, 1, 3]], float)
# Amat = A.copy()
# v = array([-4, 3, 9, 7], float)
A = array([[0, 1, 4, 1],
            [3, 4, -1, -1],
            [1, -4, 1, 5],
            [2, -2, 1, 3]],float)
v = array([-4, 3, 9, 7],float)

x, L, U, swaps = gaussElim(A,v,opts = 'LU')

# print(L@U)
# print(Amat)
print(x)
# print(L)
# print(U)
