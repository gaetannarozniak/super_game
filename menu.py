import pygame
from config import MENU_WIDTH, SCREEN_HEIGHT
from utils import Button, Font

class Menu:
    def __init__(self, change_turn, buy_miner, buy_soldier):
        self.bar_width = 3
        self.menu_width = MENU_WIDTH - self.bar_width

        change_turn_button = Button(10, 300, self.menu_width - 20,
                                          30, change_turn, text="End Turn")
        buy_miner_button = Button(10, 450, self.menu_width - 20,
                                          30, buy_miner, text="Buy Miner")
        buy_soldier_button = Button(10, 500, self.menu_width - 20,
                                          30, buy_soldier, text="Buy Soldier")
        self.button_list = [change_turn_button, buy_miner_button, buy_soldier_button]

    def draw(self, surface, teams, turn, size="medium"):
        if teams[turn].get_name() == "Red":
            surface.fill((255, 150, 150))
        else:
            surface.fill((150, 150, 255))

        pygame.draw.rect(surface, (0, 0, 0), (MENU_WIDTH - self.bar_width, 0, self.bar_width, SCREEN_HEIGHT))

        surface.blit(Font.render("Team turn : " + teams[turn].get_name(), size), 
                     (self.menu_width // 2 - Font.render("Team turn : " + teams[turn].get_name(), size).get_width() // 2, 10))
        surface.blit(Font.render("Gold : " + str(teams[turn].get_gold()), size), 
                     (self.menu_width // 2 - Font.render("Gold : " + str(teams[turn].get_gold()), size).get_width() // 2, 50))
        surface.blit(Font.render("Team " + teams[0].get_name() + " Life : " + str(teams[0].get_life()), size), 
                     (self.menu_width // 2 - Font.render("Team " + teams[0].get_name() + " Life : " + str(teams[0].get_life()), size).get_width() // 2, 150))
        surface.blit(Font.render("Team " + teams[1].get_name() + " Life : " + str(teams[1].get_life()), size), 
                     (self.menu_width // 2 - Font.render("Team " + teams[1].get_name() + " Life : " + str(teams[1].get_life()), size).get_width() // 2, 175))
        
        for button in self.button_list:
            button.draw(surface, size)

    def click(self, click_x, click_y):
        for button in self.button_list:
            if button.rect.collidepoint((click_x, click_y)):
                button.callback()

