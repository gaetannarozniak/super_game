import pygame
from .config import TILE_SIZE, TERRAINS
from .utils import load_images

import random

TERRAIN_IMAGES = load_images("terrain", TERRAINS+["flowers", "grass_2"])

class Terrain:
    def __init__(self, terrain_type:str):
        self.terrain_type = terrain_type
        self.seed = random.randint(0, 1000)

    def get_terrain_type(self):
        return self.terrain_type
    
    def set_terrain_type(self, terrain_type):
        self.terrain_type = terrain_type
    
    def draw(self, figure, i, j, accessible=False):
        random.seed(self.seed)
        if random.random() < 0.2 and self.terrain_type == "grass":
            figure.blit(TERRAIN_IMAGES["grass"], (i * TILE_SIZE, j * TILE_SIZE))
        elif random.random() > 0.9 and self.terrain_type == "grass":
            figure.blit(TERRAIN_IMAGES["flowers"], (i * TILE_SIZE, j * TILE_SIZE))
        else:
            figure.blit(TERRAIN_IMAGES["grass_2"], (i * TILE_SIZE, j * TILE_SIZE))

        if self.terrain_type != "grass":
            figure.blit(TERRAIN_IMAGES[self.terrain_type], (i * TILE_SIZE, j * TILE_SIZE))
        if accessible:
            transparent = pygame.Surface((TILE_SIZE, TILE_SIZE))
            transparent.set_alpha(100)
            transparent.fill((50, 50, 50))
            figure.blit(transparent, (i * TILE_SIZE, j * TILE_SIZE))
        
    def is_crossable(self):
        return self.terrain_type != "tree"

    def get_rl_id(self):
        return TERRAINS.index(self.terrain_type)