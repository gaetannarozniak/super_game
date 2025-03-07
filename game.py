from map import Map
from menu import Menu
from team import Team
from display_game import DisplayGame
from config import FPS
from entities import Character

import pygame
import sys  

class Game:
    def __init__(self, list_teams):
        self.map = Map()
        self.menu = Menu(self.change_turn, self.buy_miner, self.buy_soldier)
        self.display_game = DisplayGame(self.map, self.menu)
        base_tiles = self.map.get_base_tiles()
        self.teams = [Team(list_teams[i], base_tiles[i]) for i in range(len(list_teams))]
        self.selected_character = None
        self.turn = 0

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.teams[self.turn].get_name())    
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    surface, click_x, click_y = self.display_game.find_surface(event.pos)
                    if surface == "map":
                        if event.button == 1:  # Left Click
                            self.left_click(click_x, click_y)
                        elif event.button == 3:  # Right Click
                            self.right_click(click_x, click_y)
                    elif surface == "menu":
                        self.menu.click(click_x, click_y)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.change_turn()  

            self.display_game.display(self.selected_character, self.teams[self.turn])
            clock.tick(FPS)

    def left_click(self, click_x, click_y):
        x_tile, y_tile = self.map.get_tile(click_x, click_y)
        clicked_character = self.map.tiles[x_tile][y_tile].get_character()
        if (isinstance(clicked_character, Character) and 
            clicked_character.moved == False and 
            clicked_character.get_team()==self.teams[self.turn]):
            self.selected_character = clicked_character
        else:
            self.selected_character = None

    def right_click(self, click_x, click_y):
        x_tile, y_tile = self.map.get_tile(click_x, click_y)
        if self.selected_character is not None:
            self.selected_character.move_tile(self.map.tiles[x_tile][y_tile])
            self.selected_character = None
    
    def change_turn(self):
        self.selected_character = None
        for entity in self.teams[self.turn].entities:
            if isinstance(entity, Character):
                entity.moved = False
        self.turn = (self.turn+1) % len(self.teams)
        pygame.display.set_caption(self.teams[self.turn].get_name())    

    def buy_miner(self):
        self.teams[self.turn].buy_miner()

    def buy_soldier(self):
        self.teams[self.turn].buy_soldier()
