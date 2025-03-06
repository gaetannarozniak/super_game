import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
MENU_WIDTH = 200
MAP_WIDTH = SCREEN_WIDTH - MENU_WIDTH  # Largeur de la carte
MAP_HEIGHT = SCREEN_HEIGHT  # Hauteur de la carte

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (50, 200, 50)
GOLD = (255, 215, 0)
BLUE = (50, 50, 200)

class DisplayGame:
    def __init__(self, map):
        self.map = map
        self.screen = pygame.display.set_mode((self.parameters.get_n_tiles_x() * self.parameters.get_tile_size(), self.parameters.get_n_tiles_y() * self.parameters.get_tile_size()))
        
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)


    def display(self):
        menu_surface = pygame.Surface((MENU_WIDTH, SCREEN_HEIGHT))
        menu_surface.fill(GRAY)

        map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))  # La carte occupe le reste
