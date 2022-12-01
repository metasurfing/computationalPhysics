from vpython import sphere, vector, rate, canvas
from random import randrange

#particle position
position = [0,0]

#box size
L = 101
bound = (L-1)//2

#Number of time steps
N = 1000

scene = canvas(range = L)
particle = sphere(pos=vector(position[0],position[1],0),radius=2.5)

for nn in range(0,N):
    moves = []
    if abs(position[0]-bound) > 1e-14:
        moves.append([1,0])
    if abs(position[0]+bound) > 1e-14:
        moves.append([-1,0])
    if abs(position[1]-bound) > 1e-14:
        moves.append([0,1])
    if abs(position[1]+bound) > 1e-14:
        moves.append([0,-1])
    cur_move =  moves[randrange(len(moves))]
    position[0] = position[0] + cur_move[0]
    position[1] = position[1] + cur_move[1]
    rate(10)
    particle.pos = vector(position[0],position[1],0)
