from sys import path
path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages')
from numpy import array, zeros, empty
from linearAlg import gaussElim
from pylab import plot, show, spy, figure, subplots, ylim
from banded import banded
Ni = 6
Ne = 4
Nt = Ni + Ne
Vp = 5

A = zeros([Nt, Nt], float)
v = zeros(Nt,float)
v[0] = Vp
v[1] = Vp

v[Nt-2] = 0
v[Nt-1] = 0

A[0,0] = 3
A[0,1] = -1
A[0,2] = -1
A[1,0] = -1
A[1,1] = 4
A[1,2] = -1
A[1,3] = -1
A[Nt-2,Nt-4] = -1
A[Nt-2,Nt-3] = -1
A[Nt-2,Nt-2] = 4
A[Nt-2,Nt-1] = -1
A[Nt-1,Nt-3] = -1
A[Nt-1,Nt-2] = -1
A[Nt-1,Nt-1] = 3

for nn in range(2,Nt-2):
    A[nn,nn-2] = -1
    A[nn,nn-1] = -1
    A[nn,nn] = 4
    A[nn,nn+1] = -1
    A[nn,nn+2] = -1

Ab = empty([5,Nt])
for kk in range(Nt):
    if kk >= 2:
        Ab[0,kk] = A[kk-2,kk]
    if kk >= 1:
        Ab[1,kk] = A[kk-1,kk]
    Ab[2,kk] = A[kk,kk]
    if kk<=(Nt-2):
        Ab[3,kk] = A[1+kk,kk]
    if kk<=(Nt-3):
        Ab[4,kk] = A[2+kk,kk]
x = gaussElim(A,v,opts='banded',above=2,below=2)
# x = banded(Ab,v,2,2)
fig1, ax1 = subplots()
plot(x)
ylim([0,Vp+1])
# fig2 = figure(2)
# spy(A)
show()
