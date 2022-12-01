from numpy import sin, sqrt, sum
from random import random

def f(x):
    return (sin(1/(x*(2-x))))**2

N = 10000
count = 0
for ii in range(N):
    x = 2*random()
    y = random()
    if y<f(x):
        count += 1
I_hm = 2*count/N
std_k_hm = sqrt(I_hm*(2-I_hm)/N)
print('Using the hit or miss method the integral is approximately:', I_hm)
print('The error in the integral is: ', std_k_hm)

f_mean = 0
f_mean2 = 0

for kk in range(N):
    f_cur = f(2*random())
    f_mean += f_cur
    f_mean2 += f_cur*f_cur

f_mean /= N
f_mean2 /= N

I_mv = 2*f_mean
std_f_mv = 2*sqrt(f_mean2 - f_mean*f_mean)/sqrt(N)
print('Using the mean value method the integral is approximately:', I_mv)
print('The error in the integral is: ', std_f_mv)
