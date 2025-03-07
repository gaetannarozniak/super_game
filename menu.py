import pygame
from config import MENU_WIDTH

class Menu:
    def __init__(self, change_turn, buy_miner):
        self.background_color = (100, 100, 100)
        change_turn_button = Button(10, 200, MENU_WIDTH - 20,
                                          30, change_turn, text="End Turn")
        buy_miner_button = Button(10, 300, MENU_WIDTH - 20,
                                          30, buy_miner, text="Buy Miner")
                                  
        self.button_list = [change_turn_button, buy_miner_button]

    def draw(self, surface, font, team):
        surface.fill(self.background_color)
        gold_text = font.render(f"Gold: {team.get_gold()}, Nb entities: {len(team.entities)}", True, (0, 0, 0))
        surface.blit(gold_text, (10, 10))  # Position en haut à gauche
        for button in self.button_list:
            button.draw(surface, font)

    def click(self, click_x, click_y):
        for button in self.button_list:
            if button.rect.collidepoint((click_x, click_y)):
                button.callback()

class Button:
    def __init__(self, x, y, width, height, callback, text: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.callback = callback
        self.text = text

    def draw(self, menu_surface, font):
        pygame.draw.rect(menu_surface, self.color, self.rect)
        menu_surface.blit(font.render(self.text, True, (0,0,0)), self.rect.topleft)
