import sys

sys.path.insert(0,'../Users/lukeszymanski/Documents/python/computationalPhysics/chapter-5/numericalIntegration/')
from numpy import exp, linspace, zeros, log
from pylab import figure, plot, show, xlabel, ylabel
#Part a
# def integrand(a,x):
#     return x**(a-1)*exp(-x)

#Part c: The change of variables z = x/(c+x) is zero for x = c, so c = a to put
#the peak at z = 1/2.
#Part d: This form is better because it avoids raising small or large numbers to high
#powers creating overflow issues. It has limitations when x becomes very small
#due to the use of a natural log; however, this is not an issue for accuracy since
#it drives the value to 0 (the correct behavior). The only issue is that it is
#not defined for x=0, so the original form needs to be used at x = 0.
def integrand(a,x):
    from numpy import zeros
    f = zeros(len(x))
    f[x == 0] = x[x == 0]**(a-1)*exp(-x[x == 0])
    f[x != 0] = exp((a-1)*log(x[x != 0]) - x[x != 0])
    return f

Nx = 101
Na = 3
a = linspace(2,4,Na)
x = linspace(0,5,Nx)

I = zeros([Na,Nx])

for aa in range(Na):
    I[aa,:] = integrand(a[aa],x)

fig1 = figure(1)
for aa in range(Na):
    plot(x,I[aa,:])
xlabel('x')
show()

#Part d:
from math import pi, sqrt
def gamma(a):
    import sys
    sys.path.insert(0,'../Users/lukeszymanski/Documents/python/computationalPhysics/chapter-5/numericalIntegration/')
    from numpy import exp, log
    from numInt import gaussQuadInt1D
    def integrand(z):
        x = a*z/(1-z)
        return a/(1-z)**2*exp((a-1)*log(x) - x)

    return gaussQuadInt1D(integrand,0,1,200)

gamma3by2 = gamma(3/2)

print(gamma3by2)
print(0.5*sqrt(pi))
print(gamma(3))
print(gamma(6))
print(gamma(10))
