#trapInt1D integrates a 1D function over the interval (a,b) using the trapezoidal rule
#The Trapezoidal Rule integrates a piece-wise linear approximation to a function
#the function takes in arguments:
#a - starting point
#b - ending point
#N - number of points in the interval (assumed to be even)
#func - is the function to be integrated
def trapInt1D(a,b,N,func):
    s = 0.5*func(a) + 0.5*func(b)
    h = (b-a)/N

    for k in range(1,N):
        s += func(a+k*h)
    return s*h

#simpInt1D integrates a 1D function over the interval (a,b) using Simpson's rule
#Simpson's Rule integrates a piece-wise quadratic approximation to a function
#the function takes in arguments:
#a - starting point
#b - ending point
#N - number of points in the interval (assumed to be even)
#func - is the function to be integrated
def simpInt1D(a,b,N,func):
    s = func(a)+func(b)
    se = 0
    so = 0
    h = (b-a)/N

    if(N%2==0):
        for kk in range(1,N//2+1):
            se += func(a+(2*kk-1)*h)

        for kk in range(1,N//2):
            so += func(a+2*kk*h)
    else:
        print("N most be even for this simpInt to work correctly")
        return 0

    s = s + 4*se + 2*so
    return s*h/3
