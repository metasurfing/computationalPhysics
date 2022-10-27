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

def burlisch_stoer(f,t,x0,t0,H=0,delta=1e-8):
    from numpy import array, floor, append, empty, sqrt, sum
    #Implementation of error function is on positions for a 2D problem
    if isinstance(x0,(int, float)):
        Nx = 1
    else:
        Nx = len(x0)

    if H == 0:
        H = (t[1]-t[0])/2

    N = int(floor((t[1]-t[0])/H) + 1)
    x = x0.copy()
    t = t0
    x_sol = array([x0],float)
    for tt in range(N):
        #First modified midpoint step
        x1 = x + H/2*f(x,t)
        x2 = x + H*f(x1,t+H/2)

        R1 = empty([1,Nx],float)
        R1[0] = 0.5*(x1 + x2 + 0.5*H*f(x2,t+H))
        nn = 1
        error = 2*H*delta

        while error>delta*H:
            nn += 1
            h = H/nn
            #Modified midpoint method
            x1 = x + 0.5*h*f(x,t)
            x2 = x + h*f(x1,t+h/2)
            for ii in range(nn-1):
                x1 += h*f(x2,t+(ii-1)*h)
                x2 += h*f(x1,t+(ii-1/2)*h)

            R2 = R1
            R1 = empty([nn,Nx],float)
            R1[0] = 0.5*(x1 + x2 + 0.5*h*f(x2,t+H))

            for mm in range(1,nn):
                epsilon = (R1[mm-1]-R2[mm-1])/((nn/(nn-1))**(2*mm) - 1)
                R1[mm] = R1[mm-1] + epsilon
            error = abs(sqrt(epsilon[0]**2 + epsilon[2]**2))

        x = R1[nn-1]
        x_sol = append(x_sol,[x],axis=0)
        t += H

    return x_sol
