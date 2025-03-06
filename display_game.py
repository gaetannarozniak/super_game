import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_WIDTH, MAP_WIDTH, MAP_HEIGHT

class DisplayGame:
    def __init__(self, map):
        self.map = map
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.menu_surface = pygame.Surface((MENU_WIDTH, SCREEN_HEIGHT))
        self.menu_surface.fill((100, 100, 100))
        self.menu_surface.blit(self.font.render("Menu", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 50))
        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT)) 
        self.map_rect = self.screen.blit(self.map_surface, (MENU_WIDTH, 0))

    def display(self, selected_character, team):
        self.map.draw(self.map_surface, selected_character)

        gold_text = self.font.render(f"Gold: {team.get_gold()}, Nb_characters: {len(team.characters)}", True, (0, 0, 0))
        self.map_surface.blit(gold_text, (10, 10))  # Position en haut à gauche

        self.screen.blit(self.menu_surface, (0, 0))
        self.screen.blit(self.map_surface, (MENU_WIDTH, 0))

        pygame.display.flip() 

    def click_map(self, x, y):
        return x - self.map_rect.x, y - self.map_rect.y