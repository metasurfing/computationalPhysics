def rk4(f,t,x0, t0):
    from numpy import empty
    Nt = len(t)
    if isinstance(x0,(int, float)):
        x_sol = empty([1,Nt],float)
    else:
        x_sol = empty([len(x0), Nt], float)

    x = x0
    x_sol[:,0] = x0
    for tt in range(1,Nt):
        h = t[tt]-t[tt-1]
        k1 = h*f(x,t[tt-1])
        k2 = h*f(x+0.5*k1,t[tt-1]+0.5*h)
        k3 = h*f(x+0.5*k2,t[tt-1]+0.5*h)
        k4 = h*f(x+k3, t[tt-1]+h)
        x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
        x_sol[:,tt] = x

    return x_sol
