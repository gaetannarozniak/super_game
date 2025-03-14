from .config import N_TILES_X, N_TILES_Y, TILE_SIZE, BASE_COORDS
from .generate_map import generate_map
from collections import deque

class Map:
    def __init__(self, seed=None):
        self.seed = seed
        self.nb_gold = (N_TILES_X * N_TILES_Y) // 10
        self.tiles = self.generate(self.seed)
    
    def generate(self, seed):
        return generate_map(seed=seed)
        
    def draw(self, figure, selected_character):
        accessible_tiles = []
        if selected_character is not None:
            accessible_tiles = self.get_accessible_tiles(selected_character)
        
        for tile in [tile for line in self.tiles for tile in line]:
            is_accessible = tile in accessible_tiles
            tile.draw(figure, is_accessible)

    def get_tile(self, x, y):
        i, j = x // TILE_SIZE, y // TILE_SIZE
        return self.tiles[i][j]

    def get_tile_ij(self, i, j): 
        if i<0 or i>=N_TILES_X or j<0 or j>=N_TILES_Y:
            raise ValueError(f"The tile ({i}, {j}) does not exist")
        return self.tiles[i][j]

    def get_tile_array(self):
        return self.tiles

    def get_accessible_tiles(self, character):
        reachable_tiles = self.get_reachable_tiles(character)
        accessible_tiles = [tile for tile in reachable_tiles if tile.is_occupiable(character)]
        return accessible_tiles

    def get_reachable_tiles(self, character):
        queue = deque([character.get_tile()])
        visited = set()
        visited.add(character.get_tile())

        for _ in range(character.get_speed()):
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbour in self.neighbours(node):
                    if neighbour not in visited and neighbour.is_crossable(character):
                        queue.append(neighbour)
                    visited.add(neighbour)
        
        return list(visited)

    
    def neighbours(self, tile):
        neighbours = []
        for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            try:
                neighbours.append(self.get_tile_ij(tile.i + di, tile.j + dj))
            except ValueError:
                pass 
        return neighbours
    
    def get_base_tiles(self): # return the tiles of the teams base
        return [self.tiles[i][j] for (i, j) in BASE_COORDS]

    def get_dimensions(self):
        return (N_TILES_X, N_TILES_Y)