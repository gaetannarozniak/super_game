import pygame

from config import TILE_SIZE, TERRAINS
IMAGES_TERRAINS = {key: pygame.image.load(f"images/{key}.png") for key in TERRAINS}

class Terrain:
    def __init__(self, terrain_type:str):
        self.terrain_type = terrain_type

    def get_terrain_type(self):
        return self.terrain_type
    
    def draw(self, screen, x, y, accessible=False):
        tile_size = TILE_SIZE
        screen.blit(pygame.transform.scale(IMAGES_TERRAINS["grass"], (tile_size, tile_size)), (x * tile_size, y * tile_size))
        if self.terrain_type != "grass":
            screen.blit(pygame.transform.scale(IMAGES_TERRAINS[self.terrain_type], (tile_size, tile_size)), (x * tile_size, y * tile_size))
        if accessible:
            pygame.draw.rect(screen, (0, 0, 0), (x * tile_size, y * tile_size, tile_size, tile_size), 1)
        