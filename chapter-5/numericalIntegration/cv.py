def cv(T ,ThetaD, V, rho, N, x, w):
    from math import exp
    from numInt import gaussQuadInt1D
    kB = 1.380649*10**-23
    def f(x):
        return (x**4)*exp(x)/((exp(x)-1)**2)
    int = gaussQuadInt1D(f,0,ThetaD/T,N,x,w)
    return 9*V*rho*kB*(T/ThetaD)**3*int
