from math import sqrt, exp
from numpy import empty
from vpython import sphere, curve, vector, canvas, rate
from random import random, randrange


N = 25
R = 0.02

Tmax = 10.0
Tmin = 1e-3
tau = 1e4

#Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

#Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s

#Choose N city locations and calculate the initial distance
r = empty([N+1,2],float)
rplot = []

for i in range(N):
    r[i,0] = random()
    r[i,1] = random()
    rplot.append(vector(r[i,0],r[i,1],0))

r[N] = r[0]
rplot.append(vector(r[0,0],r[0,1],0))
D = distance()

#Setup the graphics
canvas(center = vector(0.5,0.5,0))
for i in range(N):
    sphere(pos=rplot[i],radius = R)
l = curve(pos=rplot,radius=R/2)

#Main loop
t = 0
T = Tmax
while T>Tmin:
    t += 1
    T = Tmax*exp(-t/tau) #Cooling

    if t%100==0: #Update the visualization every 100 moves
        l.clear()
        l = curve(pos=rplot,radius=R/2)
        rate(25)

    #Choose two cities to swap and make sure they are distinct
    i, j = randrange(1,N), randrange(1,N)

    while i == j:
        i,j = randrange(1,N), randrange(1,N)

    #Swap the two cities and calculate the change in distance
    oldD = D
    r[i,0], r[j,0] = r[j,0],r[i,0]
    r[i,1], r[j,1] = r[j,1],r[i,1]

    D = distance()
    deltaD = D-oldD

    #If the move is rejected, swap them back again
    if random()>=exp(-deltaD/T):
        r[i,0], r[j,0] = r[j,0],r[i,0]
        r[i,1], r[j,1] = r[j,1],r[i,1]
        D = oldD

    rplot[i] = vector(r[i,0],r[i,1],0)
    rplot[j] = vector(r[j,0],r[j,1],0)
