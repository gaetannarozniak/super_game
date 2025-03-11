import pygame
from game.config import MAP_WIDTH, MAP_HEIGHT

class DisplayGameRL:
    def __init__(self, map, screen):
        self.map = map
        self.screen = screen
        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) 

    def display(self, selected_character):
        self.map.draw(self.map_surface, selected_character)
        self.screen.blit(self.map_surface, (0, 0))
        pygame.display.flip()