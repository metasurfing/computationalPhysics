#This is a set of functions for calculating Fourier Transforms
def real_dft(y):
    from numpy import zeros, exp, arange, sum, conjugate
    from math import pi

    N = len(y)
    c = zeros(N,complex)
    n = arange(N)

    for kk in range(N//2+1):
        c[kk] = sum(y*exp(-2j*pi*kk*n/N))

    for kk in range(N//2+1,N):
        r = N-kk
        c[kk] = conjugate(c[r])
    return c

def real_idft(c):
    from numpy import zeros, exp, arange, sum, conjugate
    from math import pi
    N = len(c)
    y = zeros(N,float)
    n = arange(N)
    for kk in range(N):
        y[kk] = 1/N*sum(c*exp(1j*2*pi*n*kk/N))
    return y

def dct(y):

    from numpy.fft import rfft
    from numpy import empty, arange, exp, real, pi
    N = len(y)
    y2 = empty(2*N, float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]
    c = rfft(y2)
    phi = exp(-1j*pi*arange(N)/(2*N))
    return real(phi*c[:N])

def idct(a):
    from numpy.fft import irfft
    from numpy import empty, arange, exp, real, pi
    N = len(a)
    c = empty(N+1, complex)
    phi = exp(1j*pi*arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]

def fastFT(y):
    #This is a first version that is not in place
    from numpy import empty, log10, arange, pi, exp
    N = len(y)
    mp1_coeff = empty(N,complex)
    m_coeff = empty(N,complex)

    M = int(log10(N)/log10(2))
    mp1_coeff = y
    for mm in range(M-1,-1,-1):
        K = int(N/(2**mm))
        J = int(2**mm)
        for jj in range(J):
            for kk in range(K):
                kp = int(kk%(N/2**(mm+1)))
                coeffj = int(2**(mm+1)*kp + jj)
                coeffjp2m = int(coeffj + 2**mm)
                m_coeff[(2**mm)*kk + jj] = mp1_coeff[coeffj] + mp1_coeff[coeffjp2m]*exp(-1j*2*pi*kk*(2**mm)/N)
        mp1_coeff = m_coeff.copy()
    return m_coeff
