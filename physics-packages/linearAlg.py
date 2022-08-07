#This is a useful functions for solving linear equations
def gaussElim(A,v,opts = 'partial-pivot'):
    from numpy import array, empty, argmax, dot
    if(opts == 'partial-pivot'):
        N = len(v)
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
        x = 0
        L = 0
        U = 0
        output_tuple = [x,L,U]
    else:
        print('The option you have selected is not supported')
        output_tuple = []

    return output_tuple
