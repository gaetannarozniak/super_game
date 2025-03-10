import random
from config import N_TILES_X, N_TILES_Y, MINER_SPEED, BASE_COORDS
from terrains import Terrain
from tile import Tile
import numpy as np
from perlin_numpy import generate_fractal_noise_2d # pip3 install git+https://github.com/pvigier/perlin-numpy

def is_near_base(i, j):
    def d(i1, j1, i2, j2):
        return abs(i1-i2) + abs(j1-j2)

    return min([d(i, j, i_base, j_base) for (i_base, j_base) in BASE_COORDS]) <= MINER_SPEED
        

def generate_map(gold_threshold=-0.5, tree_threshold=0.25, res=5, seed=np.random.randint(1000)): # gold < grass < tree 
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

    
    
    return [[Tile(x, y, Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 
    




    



def generate_map_old(distance_base=4, group_sizes=[2,3], forest_count=5, forest_sizes=[2,3,4]):
    """
    Generates the map with grass, gold groups, and forest clusters.

    Parameters:
    - distance_base (int): Minimum distance between bases and golds.
    - group_sizes (list): Possible sizes for gold groups.
    - forest_count (int): Number of forest clusters to generate.
    - forest_sizes (list): Possible sizes for forest clusters.
    
    Returns:
    - A 2D list of Tile objects representing the generated map.
    """
    
    # Initialize all tiles as grass
    tiles_type = [["grass" for _ in range(N_TILES_Y)] for _ in range(N_TILES_X)]
    
    # Place gold groups
    golds = 0
    nb_gold = (N_TILES_X * N_TILES_Y) // 10
    while golds < nb_gold:
        x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
        if tiles_type[x][y] != "grass":
            continue  

        # Ensure gold is not too close to bases
        if abs(x - 1) + abs(y - 1) <= distance_base or abs(x - N_TILES_X + 2) + abs(y - N_TILES_Y + 2) <= distance_base:
            continue
        
        group_size = random.choice(group_sizes)
        positions = [(x, y)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(directions)  
        
        for dx, dy in directions:
            if len(positions) >= group_size:
                break
            nx, ny = x + dx, y + dy
            if 0 <= nx < N_TILES_X and 0 <= ny < N_TILES_Y and tiles_type[nx][ny] == "grass":
                positions.append((nx, ny))

        if len(positions) == group_size:
            for px, py in positions:
                tiles_type[px][py] = "gold"
                golds += 1

    # Place forest clusters
    for _ in range(forest_count):
        x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
        if tiles_type[x][y] != "grass":
            continue  

        forest_size = random.choice(forest_sizes)
        positions = [(x, y)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(directions)  
        
        for dx, dy in directions:
            if len(positions) >= forest_size:
                break
            nx, ny = x + dx, y + dy
            if 0 <= nx < N_TILES_X and 0 <= ny < N_TILES_Y and tiles_type[nx][ny] == "grass":
                positions.append((nx, ny))

        if len(positions) == forest_size:
            for px, py in positions:
                tiles_type[px][py] = "tree"

    # Convert the 2D list into Tile objects
    return [[Tile(x, y, Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 
