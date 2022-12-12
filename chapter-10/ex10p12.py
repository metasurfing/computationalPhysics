from random import random
from math import pi, acos, cos, sin
from pylab import axes, show, figure

#The ranges are 0<theta<pi and 0<phi<2*pi

#The formula for random phi is:
def phi(z):
    return 2*pi*z

#The formula for random theta is:
def theta(z):
    return acos(1-2*z)

N = 500

#Set up plot
fig = figure()
ax = axes(projection = '3d')

for nn in range(N):
    theta_cur = theta(random())
    phi_cur = phi(random())

    x = sin(theta_cur)*cos(phi_cur)
    y = sin(theta_cur)*sin(phi_cur)
    z = cos(theta_cur)

    ax.scatter(x,y,z)

show()
