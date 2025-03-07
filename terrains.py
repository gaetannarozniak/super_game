import pygame
from config import TILE_SIZE, TERRAINS
from utils import load_images

TERRAIN_IMAGES = load_images("terrain", TERRAINS)

class Terrain:
    def __init__(self, terrain_type:str):
        self.terrain_type = terrain_type

    def get_terrain_type(self):
        return self.terrain_type
    
    def set_terrain_type(self, terrain_type):
        self.terrain_type = terrain_type
    
    def draw(self, figure, x, y, accessible=False):
        figure.blit(TERRAIN_IMAGES["grass"], (x * TILE_SIZE, y * TILE_SIZE))
        if self.terrain_type != "grass":
            figure.blit(TERRAIN_IMAGES[self.terrain_type], (x * TILE_SIZE, y * TILE_SIZE))
        if accessible:
            transparent = pygame.Surface((TILE_SIZE, TILE_SIZE))
            transparent.set_alpha(100)
            transparent.fill((50, 50, 50))
            figure.blit(transparent, (x * TILE_SIZE, y * TILE_SIZE))
        
    def is_crossable(self):
        return self.terrain_type != "tree"