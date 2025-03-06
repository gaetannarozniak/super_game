import pygame
from config import MENU_WIDTH

class Menu:
    def __init__(self):
        self.color = (100, 100, 100)
        self.button = pygame.Rect(10, 200, MENU_WIDTH - 20, 30)
        self.button_color = (200, 200, 200)
        self.hover_color = (150, 150, 150)

    def display(self, screen, font, team):
        screen.fill(self.color)
        gold_text = font.render(f"Gold: {team.get_gold()}, Nb_characters: {len(team.characters)}", True, (0, 0, 0))
        screen.blit(gold_text, (10, 10))  # Position en haut à gauche
        screen.blit(font.render("Menu", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 50))
        pygame.draw.rect(screen, self.button_color, self.button)
        screen.blit(font.render("End Turn", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 200))

    def click(self, click_x, click_y):
        return self.button.collidepoint((click_x, click_y))