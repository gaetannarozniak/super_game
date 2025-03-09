from map import Map
from menu import Menu
from team import Team
from display_game import DisplayGame
from entities import Character

import pygame

class Game:
    def __init__(self, list_teams, screen):
        self.map = Map()
        self.menu = Menu(self.change_turn, self.buy_miner, self.buy_soldier)

        self.display_game = DisplayGame(self.map, self.menu, screen)

        base_tiles = self.map.get_base_tiles()
        self.teams = [Team(list_teams[i], base_tiles[i]) for i in range(len(list_teams))]
        self.selected_character = None
        self.turn = 0

    def handle_event(self, event):  
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
            if event.key == pygame.K_RETURN:
                self.change_turn()  
            if event.key == pygame.K_n:
                self.select_next_character()
            if event.key == pygame.K_m:
                self.buy_miner()
            if event.key == pygame.K_s:
                self.buy_soldier()

        if self.teams[0].get_life() == 0:
            return "Blue"
        elif self.teams[1].get_life() == 0:
            return "Red"
        return False

    def display(self):
        self.display_game.display(self.selected_character, self.teams, self.turn)

    def left_click(self, click_x, click_y):
        tile_clicked = self.map.get_tile(click_x, click_y)
        clicked_character = tile_clicked.get_character()
        if (isinstance(clicked_character, Character) and 
            clicked_character.moved == False and 
            clicked_character.get_team()==self.teams[self.turn]):
            self.selected_character = clicked_character
        else:
            self.selected_character = None

    def right_click(self, click_x, click_y):
        tile_clicked = self.map.get_tile(click_x, click_y)
        if self.selected_character is not None:
            if tile_clicked in self.map.get_accessible_tiles(self.selected_character):
                self.selected_character.move_tile(tile_clicked)
                self.select_next_character()
    
    def change_turn(self):
        self.selected_character = None
        for entity in self.teams[self.turn].entities:
            if isinstance(entity, Character):
                entity.moved = False
        self.turn = (self.turn+1) % len(self.teams)
        self.select_next_character()

    def buy_miner(self):
        new_miner = self.teams[self.turn].buy_miner()
        self.selected_character = new_miner

    def buy_soldier(self):
        new_soldier = self.teams[self.turn].buy_soldier()
        self.selected_character = new_soldier

    def select_next_character(self):
        self.selected_character = self.teams[self.turn].get_next_character(self.selected_character)