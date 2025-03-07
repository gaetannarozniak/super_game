from terrains import Terrain
from entities import Character, Building

class Tile:
    def __init__(self, x, y, terrain:Terrain = Terrain("grass")):
        self.x = x
        self.y = y
        self.character = None
        self.building = None
        self.terrain = terrain

    def draw(self, figure, accessible=False):
        self.terrain.draw(figure, self.x, self.y, accessible)
        if self.building is not None:
            self.building.draw(figure, self.x, self.y)
        if self.character is not None:
            self.character.draw(figure, self.x, self.y)

    def get_terrain(self):
        return self.terrain
    
    def set_terrain(self, terrain):
        self.terrain = terrain
    
    def get_character(self):
        return self.character

    def remove_character(self):
        if self.character is None:
            raise ValueError(f"there is no character to remove in the tile ({self.x}, {self.y})")
        self.character = None

    def set_character(self, character:Character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.x}, {self.y})")
        self.character = character

    def get_building(self):
        return self.building

    def remove_building(self):
        if self.building is None:
            raise ValueError(f"there is no building to remove in the tile ({self.x}, {self.y})")
        self.building = None

    def set_building(self, building:Building):
        if self.building is not None:
            raise ValueError(f"there is already an building in the tile ({self.x}, {self.y})")
        self.building = building

    def tile_dist(self, other_tile):
        return abs(self.x - other_tile.x) + abs(self.y - other_tile.y)
    
    def get_terrain_type(self):
        return self.terrain.get_terrain_type()
    
    def set_terrain_type(self, terrain_type):
        self.terrain.set_terrain_type(terrain_type)