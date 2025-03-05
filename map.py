from main import WIDTH, HEIGHT
from characters import Character
from terrains import Terrain
from math import abs

class Tile:
    def __init__(self, x, y, terrain:Terrain = None, character:Character=None):
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

    def draw(self):
        pass

    def remove_character(self):
        if self.character is None:
            raise ValueError(f"there is no character to remove in the tile ({self.x}, {self.y})")
        self.character = None

    def add_character(self, character:Character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.x}, {self.y})")
        self.character = character

    def tile_dist(self, other_tile:Tile):
        return abs(self.x - other_tile.x) + abs(self.y - other_tile.y)

class Map:
    def __init__(self, ):
        self.tiles = [[Tile(x, y) for y in range(HEIGHT)] for x in range(WIDTH)] 

    def draw(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.tiles[x][y].draw()    

