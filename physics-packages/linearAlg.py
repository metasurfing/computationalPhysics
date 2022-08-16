#This is a package for solving linear equations and other algorithms related to
#linear algebra
def gaussElim(Aa,va,opts = 'partial-pivot',above=1, below=1):
    from numpy import array, empty, argmax, dot, zeros, cdouble, copy
    N = len(va)
    A = copy(Aa)
    v = copy(va)
    array_dtype = A.dtype
    if(opts == 'partial-pivot'):
        for m in range(N):
            #Find the index of the element furthest from 0 in column m
            idx_tmp = m + argmax(abs(A[m:N,m]))

            #If idx_tmp is not column m rearrange the pivots so that it is
            if idx_tmp != m:
                Am_tmp = A[m,:].copy()
                A[m,:] = A[idx_tmp,:].copy()
                A[idx_tmp,:] = Am_tmp.copy()
                vm_tmp = v[m].copy()
                v[m] = v[idx_tmp].copy()
                v[idx_tmp] = vm_tmp.copy()

            #Normalize the mth row by the pivot value
            div = A[m,m]
            A[m,:] /= div
            v[m] /= div

            #Multiply the mth row by the pivot values on the remaining rows and
            #subtract them from the corresponding rows
            for i in range(m+1,N):
                mult = A[i,m]
                A[i,:] -= mult*A[m,:]
                v[i] -= mult*v[m]

        #Define an empty array to store solution in
        x = empty(N,array_dtype)

        #Solve for the vector by back substitution
        for m in range(N-1,-1,-1):
            x[m] = v[m] - dot(A[m,(m+1):N],x[(m+1):N])

        #Assign output tuple to return
        output_tuple = x

    elif(opts == 'LU'):
        L = zeros([N,N],dtype=array_dtype)
        U = zeros([N,N],dtype=array_dtype)
        swaps = empty(N,int)

        for m in range(N):
            #Find the index of the element furthest from 0 in column m
            idx_tmp = m + argmax(abs(A[m:N,m]))
            swaps[m] = idx_tmp

            #If idx_tmp is not column m rearrange the pivots so that it is
            if idx_tmp != m:
                Am_tmp = A[m,:].copy()
                A[m,:] = A[idx_tmp,:].copy()
                A[idx_tmp,:] = Am_tmp.copy()
                Lm_tmp = L[m,:].copy()
                L[m,:] = L[idx_tmp,:].copy()
                L[idx_tmp,:] = Lm_tmp.copy()


            #Build the lower triangular elements
            L[m:N,m] = A[m:N,m].copy()

            #Normalize the mth row by the pivot value
            div = A[m,m]
            A[m,:] /= div

            #Multiply the mth row by the pivot values on the remaining rows and
            #subtract them from the corresponding rows
            for i in range(m+1,N):
                mult = A[i,m]
                A[i,:] -= mult*A[m,:]

        #Assign the upper triangular matrix
        U = A.copy()

        #Define an empty array to store the solution in
        x = empty(N,array_dtype)
        y = empty(N,array_dtype)

        for m in range(N):
            if swaps[m] != m:
                vm_tmp = v[m].copy()
                v[m] = v[swaps[m]].copy()
                v[swaps[m]] = vm_tmp.copy()

        #Solve for the vectors by back substitution
        for m in range(0,N):
            y[m] = (v[m] - dot(L[m,0:m],y[0:m]))/L[m,m]

        for m in range(N-1,-1,-1):
            x[m] = y[m] - dot(A[m,(m+1):N],x[(m+1):N])

        #Assign output tuple to return
        output_tuple = [x,L,U,swaps]

    elif opts == 'banded':
    #implementation of Thomas algorithm for tridiagonal matrices
        N = len(v)
        idx = range(N)
        if any(A[idx,idx] == 0):
            print('Error: There is a zero on the diagonal and the \
             Thomas algorithm requires all diagonal elements to be non-zero')
            return 0

        #Forward solve
        for kk in range(N-below):

            #Normalize the kth row by the diagonal element
            A[kk,(kk+1):(kk+above+1)] /= A[kk,kk]
            v[kk] /= A[kk,kk]

            #Subtract the scaled kth row from the k+1th row
            A[kk+1,(kk+1):(kk+above+1)] -= A[kk+1,kk]*A[kk,(kk+1):(kk+above+1)]
            v[kk+1] -= A[kk+1,kk]*v[kk]

            for bb in range(2,below+1):
                #Subtract the scaled kth row from the k+1th row
                A[kk+bb,(kk+bb-1):(kk+above+1)] -= A[kk+bb,kk]*A[kk,(kk+bb-1):(kk+above+1)]
                v[kk+bb] -= A[kk+bb,kk]*v[kk]

        for kk in range(N-below,N):
            A[kk,(kk+1):N] /= A[kk,kk]
            v[kk] /= A[kk,kk]

            for jj in range(kk+1,N):
                A[jj,jj:N] -= A[jj,kk]*A[kk,jj:N]
                v[jj] -= A[jj,kk]*v[kk]

        #Backsubstitution
        x = empty(N,v.dtype)
        x[N-1] = v[N-1]
        for mm in range(N-2,-1,-1):
            x[mm] = v[mm] - dot(A[mm,(mm+1):(mm+above+1)],x[(mm+1):(mm+above+1)])

        output_tuple = x

    else:
        print('The option you have selected is not supported')
        output_tuple = []

    return output_tuple

#Function that computes the Q-R factorization of a matrix
def factQR(A):
    from numpy import zeros, shape, empty, dot
    from numpy.linalg import norm
    M, N = shape(A)
    v = zeros([M,N])

    Q = empty([M,N])
    R = zeros([M,N])

    for ii in range(M):
        v[:,ii] = A[:,ii].copy()

    for ii in range(M):
        R[ii,ii] = norm(v[:,ii],ord=2)
        Q[:,ii] = v[:,ii].copy()/R[ii,ii]

        for jj in range(ii+1,M):
            R[ii,jj] = dot(Q[:,ii],v[:,jj])
            v[:,jj] -= R[ii,jj]*Q[:,ii].copy()

    return Q, R

#Function that computes the eigenvalues and eigenvectors of a Hermitian matrix
#using the iterative QR algorithm
def eigH(A,tol=1e-6):
    from numpy import zeros, shape, diag, transpose
    from numpy.linalg import norm

    M, N = shape(A)
    V = zeros([M,N],A.dtype)
    D = zeros([M,N],A.dtype)
    Qi, Ri = factQR(A)
    off_diag = norm(Qi-diag(diag(Qi)))/((M-1)*N)
    D = Ri@Qi
    V = Qi.copy()
    while(off_diag>tol):
        Qi, Ri = factQR(D)
        V = V @ Qi
        D = Ri@Qi
        off_diag = norm(D-diag(diag(D)))/((M-1)*N)

    return D, Qi
