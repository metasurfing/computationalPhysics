from random import randrange
from numpy import empty, sum

N = 1000000
dice = empty([2,N],int)

count = 0

for ii in range(0,N):
    dice[0,ii] = randrange(1,7)
    dice[1,ii] = randrange(1,7)

    if abs(sum(dice[:,ii])-12) <= 1e-14:
        count +=1

print('The fraction of double sixes is:', count/N)
print('1/36 =', 1/36)
