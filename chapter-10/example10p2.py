from math import sqrt, pi, log, cos, sin
from random import random

#Constants
Z = 79
e = 1.602e-19
E = 7.7e6*e
epsilon0 = 8.854e-12
a0 = 5.292e-11
sigma = a0/100
N = 1000000

#Function to generate the gaussian distribution
def gaussian():
    r = sqrt(-2*sigma**2*log(1-random()))
    theta = 2*pi*random()
    x = r*cos(theta)
    y = r*sin(theta)
    return x, y

#Calculate the number of reflected alpha particles
b = Z*e*e/(2*pi*epsilon0*E)
count = 0
for jj in range(0,N):
    x, y = gaussian()
    rad = sqrt(x*x + y*y)
    if rad < b:
        count += 1

print(count, 'out of ', N, 'alpha particles were reflected')
print('Or ', count/N*100, 'percent')
