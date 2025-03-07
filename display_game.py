import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_WIDTH, MAP_WIDTH, MAP_HEIGHT

class DisplayGame:
    def __init__(self, map, menu, screen, font):
        self.map = map
        self.menu = menu
        self.screen = screen
        self.font = font

        self.menu_surface = pygame.Surface((MENU_WIDTH, SCREEN_HEIGHT))
        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) 

        self.rect_dict = {
            "menu": pygame.Rect(0, 0, MENU_WIDTH, SCREEN_HEIGHT),
            "map": pygame.Rect(MENU_WIDTH, 0, MAP_WIDTH, SCREEN_HEIGHT)
        }

    def display(self, selected_character, teams, turn):
        self.map.draw(self.map_surface, selected_character)
        self.menu.draw(self.menu_surface, self.font, teams, turn)

        self.screen.blit(self.menu_surface, self.rect_dict["menu"].topleft)
        self.screen.blit(self.map_surface, self.rect_dict["map"].topleft)
        pygame.display.flip()

    def find_surface(self, pos):
        x, y = pos
        for surface_name, rect in self.rect_dict.items():
            if rect.collidepoint(pos):
                local_x, local_y = x - rect.x, y - rect.y  # Convert to local coordinates
                return surface_name, local_x, local_y

        raise ValueError(f"no surface corresponds to the click ({x}, {y})")

