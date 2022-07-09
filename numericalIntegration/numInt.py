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
