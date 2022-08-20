#This is a package for solving nonlinear equations
def relaxationNd(func,x,tol = 1e-6):
    from numpy import amax, ones
    nvars = len(x)
    error = ones(nvars,float)

    m2 = func(x)
    m1 = func(m2)

    while(amax(abs(error))>tol):
        m0 = func(m1)
        if(2*m1-m2-m0 == 0):
            return m0
        error = (m1 - m0)**2/(2*m1-m2-m0)
        m1, m2 = m0, m1

    return m0
