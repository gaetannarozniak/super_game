import pygame
from config import MENU_WIDTH
from utils import Button, Font

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

    def draw(self, surface, teams, turn, size="medium"):
        surface.fill(self.background_color)
        surface.blit(Font.render("Team turn :" + teams[turn].get_name(), size), (10, 10))
        surface.blit(Font.render("Gold: " + str(teams[turn].get_gold()), size), (10, 50))
        surface.blit(Font.render("Team " + teams[0].get_name() + " Life: " + str(teams[0].get_life()), size), (10, 150))
        surface.blit(Font.render("Team " + teams[1].get_name() + " Life: " + str(teams[1].get_life()), size), (10, 175))

        for team in teams:
            if team.get_life() <= 0:
                surface.blit(Font.render(team.get_name() + " has lost", size), (10, 225))
        
        for button in self.button_list:
            button.draw(surface, size)

    def click(self, click_x, click_y):
        for button in self.button_list:
            if button.rect.collidepoint((click_x, click_y)):
                button.callback()

