import pygame
from .config import TILE_SIZE

def load_images(prefix, string_list, size_x = TILE_SIZE, size_y = TILE_SIZE):
    images = {key: pygame.image.load(f"game/resources/images/{prefix}/{key}.png") for key in string_list}
    for key in images.keys():
        images[key] = pygame.transform.scale(images[key], (size_x, size_y)) 
    return images

class Font:
    _font = {}
    
    @staticmethod
    def load():
        Font._font["small"] = pygame.font.Font(None, 15)
        Font._font["medium"] = pygame.font.Font("game/resources/font/font_medium.otf", 20)
        Font._font["large"] = pygame.font.Font("game/resources/font/font_large.ttf", 35)
    
    @staticmethod
    def render(text, size, color= (0, 0, 0)):
        return Font._font[size].render(text, True, color)
    
class Button:
    def __init__(self, x, y, width, height, callback, text: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.border_color = (255, 255, 255)
        self.callback = callback
        self.text = text

    def draw(self, surface, size):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            transparent = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            pygame.draw.rect(transparent, (50, 50, 50, 100), (0, 0, self.rect.width, self.rect.height), border_radius=15)
            surface.blit(transparent, (self.rect.x, self.rect.y))
        pygame.draw.rect(surface, self.border_color, self.rect, 2, border_radius=15)
        text_surface = Font.render(self.text, size)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        