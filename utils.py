import pygame
from config import TILE_SIZE

def load_images(prefix, string_list):
    images = {key: pygame.image.load(f"images/{prefix}/{key}.png") for key in string_list}
    for key in images.keys():
        images[key] = pygame.transform.scale(images[key], (TILE_SIZE, TILE_SIZE)) 
    return images

class Font:
    _font = {}

    @staticmethod
    def load():
        Font._font["small"] = pygame.font.Font(None, 15)
        Font._font["medium"] = pygame.font.Font(None, 25)
        Font._font["large"] = pygame.font.Font(None, 35)
    
    @staticmethod
    def render(text, size, color= (0, 0, 0)):
        return Font._font[size].render(text, True, color)
    
class Button:
    def __init__(self, x, y, width, height, callback, text: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.callback = callback
        self.text = text

    def draw(self, surface, size):
        pygame.draw.rect(surface, self.color, self.rect) 
        text_surface = Font.render(self.text, size)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)