from config import N_TILES_X, N_TILES_Y, TILE_SIZE 
from generate_map import generate_map

class Map:
    def __init__(self):
        self.nb_gold = (N_TILES_X * N_TILES_Y) // 10
        self.tiles = self.generate()
    
    def generate(self):
        return generate_map(self)
        
    def draw(self, figure, selected_character):
        accessible_tiles = []
        if selected_character is not None:
            speed = selected_character.get_speed() 
            accessible_tiles = self.get_accessible_tiles(selected_character.get_tile(), speed)

        for x in range(N_TILES_X):
            for y in range(N_TILES_Y):
                self.tiles[x][y].draw(figure, (x, y) in accessible_tiles) 

    def get_tile(self, click_x, click_y):
        return click_x // TILE_SIZE, click_y // TILE_SIZE

    def get_tile_ij(self, i, j): 
        return self.tiles[i][j]

    def get_accessible_tiles(self, tile, speed):
        accessible_tiles = []
        for x in range(N_TILES_X):
            for y in range(N_TILES_Y):
                if self.tiles[x][y].get_character() is None and tile.tile_dist(self.tiles[x][y]) <= speed:
                    accessible_tiles.append((x, y))
        return accessible_tiles
    
    def get_base_tiles(self): # return the tiles of the teams base
        return [self.tiles[3][3], self.tiles[N_TILES_X-4][N_TILES_Y-4]]