def rk4(f,t,x0, t0, h = [],type = 'none'):
    from numpy import empty

    if type == 'none':
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

    elif type == 'fixed':
        from numpy import rint
        Nt = int(rint((t[1]-t[0])/h)+1)

        if isinstance(x0,(int, float)):
            x_sol = empty([1,Nt],float)
        else:
            x_sol = empty([len(x0), Nt], float)

        x = x0.copy()
        x_sol[:,0] = x0

        tm1 = t[0]
        for tt in range(1,Nt):
            k1 = h*f(x,tm1)
            k2 = h*f(x+0.5*k1,tm1+0.5*h)
            k3 = h*f(x+0.5*k2,tm1+0.5*h)
            k4 = h*f(x+k3, tm1+h)
            x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
            x_sol[:,tt] = x
            tm1 += h

    else:
        print('{} is not a valid solution type'.format(type))
        x_sol = []


    return x_sol

def leapfrog(f,t,x0,h):
    from numpy import empty
    Nt = int((t[1]-t[0])//h + 1)

    if isinstance(x0,(int, float)):
        Nx = 1
    else:
        Nx = len(x0)

    x_sol = empty([Nx, Nt], float)
    t_sol = empty(Nt,float)

    xt = x0.copy()
    x = x0.copy()
    x_sol[:,0] = x0.copy()
    tk = t[0]

    x += h/2*f(xt,tk)

    for tt in range(1,Nt):
        tk += h/2
        xt += h*f(x,tk)
        x_sol[:,tt] = xt.copy()
        tk += h/2
        t_sol[tt] = tk
        x += h/2*f(xt,tk)

    return [x_sol, t_sol]

def verlet(f,t,x0,v0,t0,h):
    from numpy import empty
    Nt = int((t[1]-t[0])//h + 1)

    if isinstance(x0,(int, float)):
        Nx = 1
    else:
        Nx = len(x0)

    x_sol = empty([Nx, Nt], float)
    v_sol = empty([Nx, Nt], float)
    t_sol = empty(Nt,float)

    v_sol[:,0] = v0
    x_sol[:,0] = x0
    t_sol[0] = t0

    x = x0.copy()
    v = v0.copy()
    tx = t0
    v += h/2*f(x,tx)


    for tt in range(1,Nt):
        x += h*v
        tx += h
        t_sol[tt] = tx
        x_sol[:,tt] = x.copy()
        k = h*f(x,tx)
        v_sol[:,tt] = v + k/2
        v += k

    return [x_sol, v_sol, t_sol]
