import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_WIDTH, MAP_WIDTH, MAP_HEIGHT

class DisplayGame:
    def __init__(self, map, menu):
        self.map = map
        self.menu = menu

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.menu_surface = pygame.Surface((MENU_WIDTH, SCREEN_HEIGHT))
        self.menu_rect = self.screen.blit(self.menu_surface, (0, 0))

        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) 
        self.map_rect = self.screen.blit(self.map_surface, (MENU_WIDTH, 0))

    def display(self, selected_character, team):
        self.map.draw(self.map_surface, selected_character)
        self.menu.display(self.menu_surface, self.font, team)

        self.screen.blit(self.menu_surface, (0, 0))
        self.screen.blit(self.map_surface, (MENU_WIDTH, 0))

        pygame.display.flip()

    def find_surface(self, pos):
        if self.map_rect.collidepoint(pos):
            return "map", pos[0] - self.map_rect.x, pos[1] - self.map_rect.y
        return "menu", pos[0] - self.menu_rect.x, pos[1] - self.menu_rect.y