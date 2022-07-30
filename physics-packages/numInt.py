#trapInt1D integrates a 1D function over the interval (a,b) using the trapezoidal rule
#The Trapezoidal Rule integrates a piece-wise linear approximation to a function
#the function takes in arguments:
#a - starting point
#b - ending point
#N - number of intervals (assumed to be even)
#func - is the function to be integrated
#opt: determines if you want integrate a 'fixed' number of steps or
#     perform an 'adaptive'  or 'Romberg' integration to achieve a desired 'AbsTol'
#     given in the optional keyword arguments
def trapInt1D(func,a=0,b=1,N=4,opt='fixed',AbsTol=10**-3,pout = 0):
    s = 0.5*func(a) + 0.5*func(b)
    h = (b-a)/N

    for k in range(1,N):
        s += func(a+k*h)
    Int = s*h

    if(opt == 'fixed'):
        return Int

    elif(opt == 'adaptive'):
        hcur = h
        Ncur = N
        Intm1 = Int

        while(True):
            hm1 = hcur
            hcur = hm1/2
            Ncur = 2*Ncur
            scur = 0

            for k in range(1,Ncur,2):
                scur += func(a+k*hcur)

            Intcur = 0.5*Intm1 + scur*hcur

            err = abs(1/3*(Intcur-Intm1))
            if(pout):
                print('Current integration step: {0}, Value: {1}, Error: {2}'.format(Ncur, Intcur, err))
            if(err < AbsTol):
                return Intcur, err
            Intm1 = Intcur

    elif(opt == 'Romberg'):
        hcur = h
        Ncur = N
        Intm1 = Int
        ii = 2
        Rm1 = [Int]

        while(True):
            if(pout):
                print('R = {}'.format(Rm1))
            R = []
            hm1 = hcur
            hcur = hm1/2
            Ncur = 2*Ncur
            scur = 0

            for k in range(1,Ncur,2):
                scur += func(a+k*hcur)

            Intcur = 0.5*Intm1 + scur*hcur

            R = R + [Intcur]

            for mm in range(1,ii):
                R = R + [R[mm-1] + 1/(4**mm-1)*(R[mm-1]-Rm1[mm-1])]

            err = abs(1/(4**(ii-1)-1)*(R[ii-2]-Rm1[ii-2]))
            if(pout):
                print('Current integration step: {0}, Value: {1}, Error: {2}'.format(Ncur, R[ii-1] , err))
            if(err < AbsTol):
                if(pout):
                    print('R = {}'.format(R))
                return Intcur, err

            Intm1 = Intcur
            Rm1 = R
            ii += 1

    return 'The selected option in opt is not supported'

#Implementation of Euler-Maclaurin integration for 1D functions
#Uses the central difference formula for the derivative (found in numDiff.py)
#It is assumed that the physics-packages folder is on the path
#the function takes in arguments:
#a - starting point
#b - ending point
#N - number of intervals
#func - is the function to be integrated
def eulerMaclaurin1D(func,a=0,b=1,N=4,pout=0):
    from numDiff import finiteDiff
    h = (b-a)/N
    Dfa = finiteDiff(func,a,type = 'central')
    Dfb = finiteDiff(func,b,type = 'central')
    fa = func(a)
    fb = func(b)

    s = 0.5*(fa+fb) + h/12*(Dfa-Dfb)

    for kk in range(1,N):
        s += func(a+kk*h)
    return s*h

#simpInt1D integrates a 1D function over the interval (a,b) using Simpson's rule
#Simpson's Rule integrates a piece-wise quadratic approximation to a function
#the function takes in arguments:
#a - starting point
#b - ending point
#N - number of intervals (assumed to be even)
#func - is the function to be integrated
#opt: determines if you want integrate a 'fixed' number of steps or
#     perform an 'adaptive' integration to achieve a desired 'tolerance'
#     given in the optional keyword arguments
def simpInt1D(func,a=0,b=1,N=4,opt='fixed',AbsTol=10**-3,pout=0):
    s0 = func(a)+func(b)
    se = 0
    so = 0
    h = (b-a)/N

    if(N%2==0):
        for kk in range(1,N//2+1):
            se += func(a+(2*kk-1)*h)

        for kk in range(1,N//2):
            so += func(a+2*kk*h)
    else:
        print("N most be even for simpInt to work correctly")
        return 0

    s = s0 + 4*se + 2*so

    Int = s*h/3

    if(opt == 'fixed'):
            return Int

    elif(opt == 'adaptive'):
        hcur = h
        Ncur = N
        Intm1 = Int
        sm1 = 1/3*(s0+2*se)
        tm1 = 2/3*so

        while(True):
            hm1 = hcur
            hcur = hm1/2
            Ncur = 2*Ncur
            scur = sm1+tm1
            tcur = 0

            for k in range(1,Ncur,2):
                tcur += func(a+k*hcur)

            tcur = 2/3*tcur

            Intcur = hcur*(scur+2*tcur)

            sm1 = scur
            tm1 = tcur

            err = abs(1/15*(Intcur-Intm1))

            if(pout):
                print('Current integration step: {0}, Value: {1}, Error: {2}'.format(Ncur, Intcur, err))

            if(err < AbsTol):
                return Intcur, err

            Intm1 = Intcur

    return 'The selected option in opt is not supported'

def gaussQuadInt1D(func,a=0,b=1,N=4,xk=[],wk=[]):
    from numpy import any
    if(not (any(xk) and any(wk))):
        #Calculate sample points and weights
        xk, wk = gaussxwab(a,b,N)

    #Calculate the integral
    s = 0.0
    for k in range(N):
        s += wk[k]*func(xk[k])
    return s

def gaussQuadInt2D(func,ax=0,bx=1,ay=0,by=1,N=4,xk=[],yk=[],wkx=[],wky = []):
    from numpy import any
    if(not (any(xk) and any(wky) and any(yk) and any(wkx))):
        #Calculate sample points and weights
        xk, wkx = gaussxwab(ax,bx,N)
        yk, wky = gaussxwab(ay,by,N)

    #Calculate the integral
    s = 0.0
    #This is really inefficient but quick and dirty may want to find a way
    #to vectorize this
    for ii in range(N):
        for jj in range(N):
            s += wkx[ii]*wky[jj]*func(xk[ii],yk[jj])
    return s
#Helper function for gaussQuadInt1D
#Calculates the sample points and weights for a function defined
#over the interval [a, b]
def gaussxwab(a,b,N):
    x, w = gaussxw(N)
    return 0.5*(b-a)*x + 0.5*(b+a), 0.5*(b-a)*w

#Helper function for gaussxwab
#Calculates the sample points and weights for a function defined
#over the interval [-1, 1]
def gaussxw(N):
    from numpy import ones, copy, cos, tan, pi, linspace

    #Set up initial guesses for zeros of the Legendre Polynomials
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    #Set tolerances for Newton's method
    epsilon = 1e-15
    delta = 1.0

    #Run Newton-Raphson to find the zeroes
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1, ((2*k+1)*x*p1-k*p0)/(k+1)
        #dp = (N+1)*(p0-x*p1)/(1-x*x) #dp from the book
        dp = N/(x*x-1)*(x*p1-p0) #derivative that you derived
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    #Calculate the weights at the sample points
    w = 2/(1-x*x)/(dp*dp) # formula from book
    #w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp) #from code in the book

    return x, w
