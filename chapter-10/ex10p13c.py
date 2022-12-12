from vpython import sphere, vector, rate, canvas
from numpy import array, append, sum, any, abs, ceil, linalg, sqrt, max, cos, sin, pi
from random import randrange, random


#box size
L = 201
bound = (L-1)//2

#Set up array to hold fixed particle positions
fixed_particles = array([[0,0]])

#Possible moves
moves = [[1,0],[-1,0],[0,1],[0,-1]]

#Setup canvas for visualization
scene = canvas(range = L)

#Initialize variables for loop
pp = 0
rad_limit = 1
particle = []
rad = 0
max_radius = sqrt(2)*bound/2

while rad_limit:
    particle_free = 1

    #Current initialization radius
    rad_init = ceil(max(linalg.norm(fixed_particles,axis=1))) + 1

    if rad_init>max_radius:
        rad_limit = 0

    #Initial particle position
    theta_init = 2*pi*random()
    xpos = ceil(rad_init*cos(theta_init))
    ypos = ceil(rad_init*sin(theta_init))
    position = [xpos,ypos]

    while particle_free:
        cur_move =  moves[randrange(len(moves))]
        position[0] = position[0] + cur_move[0]
        position[1] = position[1] + cur_move[1]

        pvec = array([[position[0],position[1]]])
        #Check if the particle has attached itself to another one
        if any(sum(abs(fixed_particles - pvec),axis=1)==1):
            particle_free = 0
            particle.append(sphere(pos=vector(position[0],position[1],0),radius=2.5))
            fixed_particles = append(fixed_particles,pvec,axis=0)
            #color particles
            Np = len(particle)
            for nn in range(Np):
                cc = nn+1
                shade = 0.4+0.6*cc/Np
                particle[nn].color = vector(shade,shade,shade)

        #Check if the particle is too far away from initial radius
        if linalg.norm(pvec) >= 2*rad_init:
            particle_free = 0
