from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')

from linearAlg import factQR, eigH
from numpy import array, transpose, diag

A = array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]])

Q, R = factQR(A)

D, V = eigH(A)

print('Accuracy of QR-factorization (A-QR):')
print(abs(A-Q@R))
print('Eigenvalues of A:')
print(diag(D))
