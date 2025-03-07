import pygame
from config import TILE_SIZE

def load_images(prefix, string_list):
    images = {key: pygame.image.load(f"images/{prefix}/{key}.png") for key in string_list}
    for key in images.keys():
        images[key] = pygame.transform.scale(images[key], (TILE_SIZE, TILE_SIZE)) 
    return images