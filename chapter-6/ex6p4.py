from numpy import array, dot, empty
from numpy.linalg import solve

A = array([[4, -1, -1, -1],
           [-1, 3, 0, -1],
           [-1, 0, 3, -1],
           [-1, -1, -1, 4]],float)
Amat = A.copy()
Vp = 5
v = array([1, 0, 1, 0],float)*Vp
N = len(v)

for m in range(N):
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]

    # for i in range(m+1,N):
    #     x[m] -= A[m,i]*x[i]
    x[m] = v[m] - dot(A[m,(m+1):N],x[(m+1):N])

x_np = solve(A,v)
print(x)
print(x_np)
