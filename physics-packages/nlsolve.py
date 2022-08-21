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
