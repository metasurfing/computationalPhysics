from pylab import imshow,show,jet
from numpy import loadtxt

data = loadtxt("circular.txt",float)
imshow(data,origin = "lower",extent = [0, 10, 0, 5], aspect = 2.0)
jet()
show()
