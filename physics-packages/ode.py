def rk4(f,t,t0, x0):
    x = x0
    x_sol = []
    x_sol.append(x)
    for tt in range(1,len(t)):
        h = t[tt]-t[tt-1]
        k1 = h*f(x,t[tt-1])
        k2 = h*f(x+0.5*k1,t[tt-1]+0.5*h)
        k3 = h*f(x+0.5*k2,t[tt-1]+0.5*h)
        k4 = h*f(x+k3, t[tt-1]+h)
        x += 1/6*(k1 + 2*k2 + 2*k3 + k4)
        x_sol.append(x)

    return x_sol
