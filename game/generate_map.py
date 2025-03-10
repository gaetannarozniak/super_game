from .config import N_TILES_X, N_TILES_Y, MINER_SPEED, BASE_COORDS
from .terrains import Terrain
from .tile import Tile
import numpy as np
from perlin_numpy import generate_fractal_noise_2d # pip3 install git+https://github.com/pvigier/perlin-numpy

def is_near_base(i, j):
    def d(i1, j1, i2, j2):
        return abs(i1-i2) + abs(j1-j2)

    return min([d(i, j, i_base, j_base) for (i_base, j_base) in BASE_COORDS]) <= MINER_SPEED

def is_valid_generation(tiles):
    return True
        

def generate_map(gold_threshold=-0.5, tree_threshold=0.25, res=5, seed=np.random.randint(10000)): # gold < grass < tree 
    tiles_type = [["grass" for _ in range(N_TILES_Y)] for _ in range(N_TILES_X)]

    np.random.seed(seed)
    noise = generate_fractal_noise_2d((N_TILES_X, N_TILES_Y), (res, res), 2)
    for i in range(N_TILES_X):
        for j in range(N_TILES_Y):
            if noise[i][j] < gold_threshold and not is_near_base(i, j):
                tiles_type[i][j] = "gold"
            elif noise[i][j] > tree_threshold:
                tiles_type[i][j] = "tree"
    
    for (i, j) in BASE_COORDS:
        tiles_type[i][j] = "grass"

    
    
    result = [[Tile(x, y, Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 

    if is_valid_generation(result):
        return result
    return generate_map(gold_threshold, tree_threshold, res, seed+1)
    




    
