from main import WIDTH, HEIGHT
from characters import Character
from terrains import Terrain

class Tile:
    def __init__(self, x, y, terrain:Terrain = None, character:Character=None):
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

    def draw(self):
        pass

class Map:
    def __init__(self, ):
        self.tiles = [[Tile(x, y) for y in range(HEIGHT)] for x in range(WIDTH)] 

    def draw(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.tiles[x][y].draw()    

