import random
from config import N_TILES_X, N_TILES_Y
from terrains import Terrain
from tile import Tile

def generate_map(self, distance_base=4, group_sizes=[2,3], forest_count=5, forest_sizes=[2,3,4]):
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
