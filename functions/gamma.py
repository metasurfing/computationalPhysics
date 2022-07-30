def gamma(a):
    import sys
    sys.path.insert(0,'/Users/lukeszymanski/Documents/python/computationalPhysics/physics-packages/')
    from numpy import exp, log
    from numInt import gaussQuadInt1D
    def integrand(z):
        x = a*z/(1-z)
        return a/(1-z)**2*exp((a-1)*log(x) - x)

    return gaussQuadInt1D(integrand,0,1,200)
