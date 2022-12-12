from vpython import sphere, vector, rate, canvas
from numpy import array, append, sum, any, abs
from random import randrange


#box size
L = 101
bound = (L-1)//2

#Set up array to hold fixed particle positions
fixed_particles = array([[L,L]])
for kk in range(-bound,bound+1):
    fixed_particles = append(fixed_particles,[[-bound,kk],[kk,-bound],[bound,kk],[kk,bound]],axis=0)

#Possible moves
moves = [[1,0],[-1,0],[0,1],[0,-1]]

#Setup canvas for visualization
scene = canvas(range = L)

#Initialize variables for loop
pp = 0
center_free = 1
particle = []

while center_free:
    particle_free = 1
    #particle position
    position = [0,0]
    particle.append(sphere(pos=vector(position[0],position[1],0),radius=2.5))
    Np = len(particle)
    for nn in range(Np):
        cc = nn+1
        shade = 0.4+0.6*cc/Np
        particle[nn].color = vector(shade,shade,shade)
    while particle_free:
        cur_move =  moves[randrange(len(moves))]
        position[0] = position[0] + cur_move[0]
        position[1] = position[1] + cur_move[1]

        pvec = array([[position[0],position[1]]])
        #Check if the particle has attached itself to another one
        if any(sum(abs(fixed_particles - pvec),axis=1)==1):
            particle_free = 0
            particle[pp].pos = vector(position[0],position[1],0)
            fixed_particles = append(fixed_particles,pvec,axis=0)

    #Check to see if the particle is in the center
    if sum(abs(pvec)) == 0:
        center_free = 0
    pp += 1
