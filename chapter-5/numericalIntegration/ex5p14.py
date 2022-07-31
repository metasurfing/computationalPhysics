from numInt import gaussQuadInt2D
from physical_constant import Newton_Gravity
from numpy import linspace, zeros
from pylab import plot, show, xlabel, ylabel, figure

Ns = 101
z = linspace(0.1,10,Ns)
G = Newton_Gravity()
Fz1 = zeros(Ns)
L = 10
N = 100
sigma = 1

for kk in range(Ns):
    zk = z[kk]
    def dFz(x,y):
        return 1/(x*x + y*y + zk*zk)**(3/2)

    Fz1[kk] = gaussQuadInt2D(dFz, -L/2, L/2, -L/2, L/2, N)

Fz = G*sigma*z*Fz1
f = figure(1)
plot(z,Fz)
xlabel('z Position (m)')
ylabel('Force (N)')
show()
#part c
#The drop off is most likely due to the multiplication by z introduced by
#using cosT = z/r. The zero is located at the triple pole singularity at z = 0
#So one potential mitigation strategy could be to use the Residue Theorem to
#extract the singularity.
#Another is to not use values of z smaller than the smallest values for x and y that have been used.
