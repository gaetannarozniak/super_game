import pygame
from config import TILE_SIZE, TERRAINS

IMAGES_TERRAINS = {key: pygame.image.load(f"images/{key}.png") for key in TERRAINS}
IMAGES_TERRAINS = {key: pygame.transform.scale(IMAGES_TERRAINS[key], (TILE_SIZE, TILE_SIZE)) for key in IMAGES_TERRAINS}

class Terrain:
    def __init__(self, terrain_type:str):
        self.terrain_type = terrain_type

    def get_terrain_type(self):
        return self.terrain_type
    
    def draw(self, screen, x, y, accessible=False):
        screen.blit(IMAGES_TERRAINS["grass"], (x * TILE_SIZE, y * TILE_SIZE))
        if self.terrain_type != "grass":
            screen.blit(IMAGES_TERRAINS[self.terrain_type], (x * TILE_SIZE, y * TILE_SIZE))
        if accessible:
            pygame.draw.rect(screen, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        