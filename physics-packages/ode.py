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

    elif type == 'adaptive':
        Nt = len(t)
        if isinstance(x0,(int, float)):
            x_sol = empty([1,Nt],float)
        else:
            x_sol = empty([len(x0), Nt], float)

        x = x0
        x_sol[:,0] = x0
        for tt in range(1,Nt):
            k1 = h*f(x,t[tt-1])
            k2 = h*f(x+0.5*k1,t[tt-1]+0.5*h)
            k3 = h*f(x+0.5*k2,t[tt-1]+0.5*h)
            k4 = h*f(x+k3, t[tt-1]+h)
            x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
            x_sol[:,tt] = x
    else:
        print('{} is not a valid solution type'.format(type))
        x_sol = []


    return x_sol
