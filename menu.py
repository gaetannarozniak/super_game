import pygame
from config import MENU_WIDTH

class Menu:
    def __init__(self, change_turn, buy_miner, buy_soldier):
        self.background_color = (100, 100, 100)
        change_turn_button = Button(10, 300, MENU_WIDTH - 20,
                                          30, change_turn, text="End Turn")
        buy_miner_button = Button(10, 450, MENU_WIDTH - 20,
                                          30, buy_miner, text="Buy Miner")
        
        buy_soldier_button = Button(10, 500, MENU_WIDTH - 20,
                                          30, buy_soldier, text="Buy Soldier")
                                  
        self.button_list = [change_turn_button, buy_miner_button, buy_soldier_button]

    def draw(self, surface, font, teams, turn):
        surface.fill(self.background_color)

        self.draw_text(surface, font, "Team turn :" + teams[turn].get_name(), 10, 10)
        self.draw_text(surface, font, "Gold: " + str(teams[turn].get_gold()), 10, 50)
        self.draw_text(surface, font, "Team " + teams[0].get_name() + " Life: " + str(teams[0].get_life()), 10, 150)
        self.draw_text(surface, font, "Team " + teams[1].get_name() + " Life: " + str(teams[1].get_life()), 10, 175)

        for team in teams:
            if team.get_life() <= 0:
                self.draw_text(surface, font, team.get_name() + " has lost", 10, 225)
        
        for button in self.button_list:
            button.draw(surface, font)

    def click(self, click_x, click_y):
        for button in self.button_list:
            if button.rect.collidepoint((click_x, click_y)):
                button.callback()

    def draw_text(self, surface, font, text, x, y):
        surface.blit(font.render(text, True, (0, 0, 0)), (x, y))

class Button:
    def __init__(self, x, y, width, height, callback, text: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)
        self.callback = callback
        self.text = text

    def draw(self, menu_surface, font):
        pygame.draw.rect(menu_surface, self.color, self.rect)
        menu_surface.blit(font.render(self.text, True, (0,0,0)), self.rect.topleft)
