import pygame
from .terrains import Terrain
from .entities import Character, Building
from .config import DISPLAY_TILE_IDS, TILE_SIZE

class Tile:
    def __init__(self, i, j, terrain:Terrain = Terrain("grass")):
        self.i = i
        self.j = j
        self.character = None
        self.building = None
        self.terrain = terrain

    def draw(self, figure, accessible=False):
        self.terrain.draw(figure, self.i, self.j, accessible)
        if self.building is not None:
            self.building.draw(figure, self.i, self.j)
        if self.character is not None:
            self.character.draw(figure, self.i, self.j)
        if DISPLAY_TILE_IDS:
            font = pygame.font.Font(None, 16)
            text_surface = font.render(str(self.get_rl_id()), True, (0,0,0))
            figure.blit(text_surface, (self.i*TILE_SIZE, self.j*TILE_SIZE))

    # is it allowed for the character to pass by the tile
    def is_crossable(self, character):
        if not self.terrain.is_crossable():
            return False
        if self.character is not None and self.character.get_team() != character.get_team():
            return False
        if self.building is not None and self.building.get_team() != character.get_team():
            return False
        return True

    # is it allowed for the character to be on the tile (no matter whether the tile is reachable or not)
    def is_occupiable(self, character: Character):
        return (self.terrain.is_crossable() and 
                character.can_walk_on(self.character) and
                character.can_walk_on(self.building))

    def get_terrain(self):
        return self.terrain
    
    def set_terrain(self, terrain):
        self.terrain = terrain
    
    def get_character(self):
        return self.character

    def has_character(self):
        return self.character is not None

    def remove_character(self):
        if self.character is None:
            raise ValueError(f"there is no character to remove in the tile ({self.i}, {self.j})")
        self.character = None

    def set_character(self, character:Character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.i}, {self.j})")
        self.character = character

    def get_building(self):
        return self.building

    def remove_building(self):
        if self.building is None:
            raise ValueError(f"there is no building to remove in the tile ({self.i}, {self.j})")
        self.building = None

    def set_building(self, building:Building):
        if self.building is not None:
            raise ValueError(f"there is already an building in the tile ({self.i}, {self.j})")
        self.building = building

    def tile_dist(self, other_tile):
        return abs(self.i - other_tile.i) + abs(self.j - other_tile.j)
    
    def get_terrain_type(self):
        return self.terrain.get_terrain_type()
    
    def set_terrain_type(self, terrain_type):
        self.terrain.set_terrain_type(terrain_type)

    def get_rl_id(self):
        terrain_id = self.terrain.get_rl_id()
        character_id = 0 if self.character is None else 1 + self.character.get_rl_id()
        base_id = 0 if self.building is None else 1 + self.building.get_rl_id()
        return [terrain_id, character_id, base_id]
        
