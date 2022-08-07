from numpy import array, empty, dot

A = array([[2, 1, 4, 1],
          [3, 4, -1, -1],
          [1, -4, 1, 5],
          [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
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

print(x)
