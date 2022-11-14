from numpy import empty, sin, pi, arange, ones
from pylab import plot,xlabel,ylabel,show, legend

A = 10.0
B = 12.0
Tau = 365.0

def To(tt):
    return A + B*sin(2*pi*tt/Tau)

#Constants
L = 20
D = 0.1
N = 100
a = L/N
h = 0.1
epsilon = h/1000

Tlo = 10.0
Tmid = 10.0
Thi = 11.0

t1 = 9*365 + 91
t2 = 9*365 + 181
t3 = 9*365 + 272
t4 = 9*365 + 365
tend = t4 + epsilon

#Create arrays
T = empty(N+1, float)
T[0] = Tlo
T[N] = Thi
T[1:N] = Tmid
Tp = empty(N+1, float)
Tp[0] = Tlo
Tp[N] = Thi

#Main loop
t = 0.0
c = h*D/(a*a)

while t<tend:
    #Update the surface boundary conditions to match the current time step
    T[0] = To(t)
    Tp[0] = To(t)
    #Calculate the new values of T
    Tp[1:N] = T[1:N] + c * (T[2:N+1] + T[0:N-1] - 2*T[1:N])
    T,Tp = Tp,T
    t += h

    #Make plots at the given times
    if abs(t-t1)<epsilon:
        plot(arange(0,L,L/(N+1)),T)
    if abs(t-t2)<epsilon:
        plot(arange(0,L,L/(N+1)),T)
    if abs(t-t3)<epsilon:
        plot(arange(0,L,L/(N+1)),T)
    if abs(t-t4)<epsilon:
        plot(arange(0,L,L/(N+1)),T)

xlabel('Subsurface Depth (m)')
ylabel('Temperature (Celsius)')
legend(['Summer','Fall','Winter','Spring'])
show()
