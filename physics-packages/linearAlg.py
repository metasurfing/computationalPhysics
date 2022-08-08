#This is a useful functions for solving linear equations
def gaussElim(A,v,opts = 'partial-pivot'):
    from numpy import array, empty, argmax, dot, zeros
    N = len(v)
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
        x = empty(N,float)

        #Solve for the vector by back substitution
        for m in range(N-1,-1,-1):
            x[m] = v[m] - dot(A[m,(m+1):N],x[(m+1):N])

        #Assign output tuple to return
        output_tuple = x

    elif(opts == 'LU'):
        L = zeros([N,N])
        U = zeros([N,N])
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
        x = empty(N,float)
        y = empty(N,float)

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
    else:
        print('The option you have selected is not supported')
        output_tuple = []

    return output_tuple
