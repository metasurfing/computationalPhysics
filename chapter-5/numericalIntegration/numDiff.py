#This is a package for evaluating numerical derivatives of functions
def finiteDiff(func,x0,h = 0,type = 'forward'):
    f1 = func(x0)

    if type == 'forward':
        if h == 0:
            from math import sqrt
            h = sqrt(4*10**-16*abs(f1)) #Assumes f'' is on the order of 1
        f2 = func(x0+h)
        Dxf = (f2 - f1)/h

    elif type == 'backward':
        if h == 0:
            from math import sqrt
            h = sqrt(4*10**-16*abs(f1)) #Assumes f'' is on the order of 1
        f2 = func(x0-h)
        Dxf = (f1 - f2)/h

    elif type == 'central':
        if h == 0:
            from math import sqrt
            h = (24*10**-16*abs(f1))**(1/3) #Assumes f''' is on the order of 1
        Dxf = (func(x0+h/2) - func(x0-h/2))/h

    else:
        print ("The type of derivative requested is not supported by finiteDiff(). \
                The supported options are: 'forward', 'backward', and 'central')")
        Dxf = 0
    return Dxf
