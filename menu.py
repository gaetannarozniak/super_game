import pygame
from config import MENU_WIDTH

class Menu:
    def __init__(self, change_turn):
        self.color = (100, 100, 100)
        self.change_turn_button = Button(10, 200, MENU_WIDTH - 20, 30, change_turn)

    def draw(self, surface, font, team):
        surface.fill(self.color)
        gold_text = font.render(f"Gold: {team.get_gold()}, Nb_characters: {len(team.characters)}", True, (0, 0, 0))
        surface.blit(gold_text, (10, 10))  # Position en haut à gauche
        surface.blit(font.render("Menu", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 50))
        self.change_turn_button.draw(surface)
        surface.blit(font.render("End Turn", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 200))

    def click(self, click_x, click_y):
        if self.change_turn_button.rect.collidepoint((click_x, click_y)):
            self.change_turn_button.callback()

class Button:
    def __init__(self, x, y, width, height, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.callback = callback

    def draw(self, menu_surface):
        pygame.draw.rect(menu_surface, self.color, self.rect)