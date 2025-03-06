from map import Map
from menu import Menu
from team import Team
from display_game import DisplayGame
import pygame
from config import FPS

class Game:
    def __init__(self, list_teams):
        self.map = Map()
        self.menu = Menu()
        self.display_game = DisplayGame(self.map, self.menu)
        self.teams = [Team(name) for name in list_teams]
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
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    click_x, click_y = self.display_game.click_map(click_x, click_y)
                    self.map.generate_character(self.teams, click_x, click_y)
                    if event.button == 1:  # Left Click
                        self.left_click(click_x, click_y, self.turn)
                    elif event.button == 3:  # Right Click
                        self.right_click(click_x, click_y)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.change_turn()  

            self.display_game.display(self.selected_character, self.teams[self.turn])
            clock.tick(FPS)
        
        pygame.quit()

    def left_click(self, click_x, click_y, turn):
        x_tile, y_tile = self.map.get_tile(click_x, click_y)
        clicked_character = self.map.tiles[x_tile][y_tile].get_character()
        if clicked_character is None or (clicked_character.get_team() == self.teams[turn] and clicked_character.moved == False):
            self.selected_character = clicked_character

    def right_click(self, click_x, click_y):
        x_tile, y_tile = self.map.get_tile(click_x, click_y)
        if self.selected_character is not None:
            self.selected_character.move_tile(self.map.tiles[x_tile][y_tile])
            self.selected_character = None
    
    def change_turn(self):
        self.selected_character = None
        for character in self.teams[self.turn].characters:
            character.moved = False
        self.turn = (self.turn+1) % len(self.teams)
        pygame.display.set_caption(self.teams[self.turn].get_name())    