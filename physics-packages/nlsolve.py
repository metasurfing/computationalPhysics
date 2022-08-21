#This is a package for solving nonlinear equations
def relaxationNd(func,x,tol = 1e-6, count = 0, maxIter = 20):
    from numpy import amax, ones
    nvars = len(x)
    error = ones(nvars,float)

    m2 = func(x)
    m1 = func(m2)
    ii = 0

    while(amax(abs(error))>tol and ii < maxIter):
        m0 = func(m1)
        if count == 1:
            ii += 1
        if all(2*m1-m2-m0 == 0):
            return m0
        error = abs((m1 - m0)**2/(2*m1-m2-m0))
        m1, m2 = m0, m1
    if count == 1:
        if(ii == maxIter):
            print('Did not converge. Hit max iterations.')
        return m0, ii
    else:
        return m0

def overrelaxationNd(func,x,tol = 1e-6, count = 0, w = 0.5):
    from numpy import amax, ones
    nvars = len(x)
    error = ones(nvars,float)

    m2 = func(x)
    m1 = (1+w)*func(m2) - w*m2
    ii = 0

    while(amax(abs(error))>tol):
        m0 = (1+w)*func(m1)-w*m1
        if count == 1:
            ii += 1
        if (1+w)*(m0-m1)/(m1-m2)-w == 0:
            return m0
        error = abs((m1 - m0)/(1-1/((1+w)*(m0-m1)/(m1-m2)-w)))
        m1, m2 = m0, m1
    if count == 1:
        return m0, ii
    else:
        return m0

def binary_search(func,a,b,tol=1e-6):
    from numpy import copy
    dx = b-a
    fa = func(a)
    fb = func(b)
    error = 1
    if(fa*fb>0):
        print('Both end points have the same sign. Returning a 0')
        return 0
    elif(fa*fb<0):
        a_tmp = copy(a)
        b_tmp = copy(b)
        ii = 0
        while(error>tol):
            midpoint = (a_tmp+b_tmp)/2
            fm = func(midpoint)
            if fm == 0:
                return midpoint
            elif fm*fa<0:
                b_tmp = midpoint
            else:
                a_tmp = midpoint
            ii += 1
            error = dx/2**ii
        return (a_tmp + b_tmp)/2

    elif(fa == 0):
        return a
    else:
        return b

#Newton's method
def newton_method(func,x0, tol = 1e-6, grad = [], maxIter = 20):
    delta = 1
    xcur = x0
    fval = func(x0)
    ii = 0
    if grad == []:
        from numDiff import finiteDiff
        def grad(x):
            return finiteDiff(func,x,type = 'forward')

    while(abs(delta)>tol and ii < maxIter):
        delta = fval/grad(xcur)
        xcur -= delta
        fval = func(xcur)
        ii += 1
    if ii == maxIter:
        print('Did not converge: max iterations reached.')
    return xcur
