import pygame

TILE_SIZE = 40

TERRAINS = ["grass", "base", "gold"]
IMAGES_TERRAINS = {key: pygame.image.load(f"images/{key}.png") for key in TERRAINS}

for key in IMAGES_TERRAINS:
    IMAGES_TERRAINS[key] = pygame.transform.scale(IMAGES_TERRAINS[key], (TILE_SIZE, TILE_SIZE))

class Terrain:
    def __init__(self, terrain_type:str):
        self.terrain_type = terrain_type

    def get_terrain_type(self):
        return self.terrain_type
    
    def draw(self, screen, x, y):
        screen.blit(IMAGES_TERRAINS["grass"], (x * TILE_SIZE, y * TILE_SIZE))
        if self.terrain_type != "grass":
            screen.blit(IMAGES_TERRAINS[self.terrain_type], (x * TILE_SIZE, y * TILE_SIZE))