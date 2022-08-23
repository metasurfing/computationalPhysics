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
    xcur = x0
    dim = len(xcur)
    if dim == 1:
        delta = 1
        fval = func(x0)
        ii = 0
        if grad == []:
            from numDiff import finiteDiff
            def grad(x):
                return finiteDiff(func,x,type = 'central')

        while(abs(delta)>tol and ii < maxIter):
            if abs(grad(xcur)) > 1e-14:
                delta = fval/grad(xcur)
            else:
                print(grad(xcur))
                print('Did not converge: Hit stationary point')
                return xcur
            xcur -= delta
            fval = func(xcur)
            ii += 1
        if ii == maxIter:
            print('Did not converge: max iterations reached.')
    else:
        from numpy import ones, amax
        from linearAlg import gaussElim
        delta = ones(dim,float)
        ii  = 0
        if grad == []:
            print('You must supply a Jacobian matrix for dim > 1')
            return 0
        while(amax(abs(delta))>tol and ii < maxIter):
            delta = gaussElim(grad(xcur),func(xcur))
            xcur -= delta

    return xcur

#Secant method
def secant_method(func,x0, tol = 1e-6, maxIter = 20):
    delta = 1
    #Generate initial points to approximate the derivative
    x1 = x0
    f1 = func(x0)
    x2 = (1+1e-3)*x1
    x3 = x2
    f2 = func(x2)
    ii = 0
    while(abs(delta)>tol and ii < maxIter):
        if abs(f2-f1) < 1e-14:
            return x2
        delta = f2*(x2-x1)/(f2-f1)
        x3 -= delta
        f1 = f2
        x1 = x2
        f2 = func(x3)
        x2 = x3
        ii += 1
    if ii == maxIter:
        print('Did not converge: max iterations reached.')
    return x3

#Golden Ratio search
def golden_search(func, x1, x4, tol = 1e-6):
    from numpy import sqrt, array
    z = (1+sqrt(5))/2
    dint = x4-x1
    x2 = x4 - dint/z
    x3 = x1 + dint/z
    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)
    f4 = func(x4)

    if (f1<f2 and f1<f3) or (f4<f2 and f4<f3):
        print('The initial points don\'t bracket a minimum.')
        return array([0])

    while dint>tol:
        if f2 < f3:
            x4, f4 = x3, f3
            x3, f3 = x2, f2
            dint = x4-x1
            x2 = x4 - dint/z
            f2 = func(x2)
        else:
            x1, f1 = x2, f2
            x2, f2, = x3, f3
            dint = x4 - x1
            x3 = x1 + dint/z
            f3 = func(x3)

    return 0.5*(x1+x4)
