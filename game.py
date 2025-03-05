from map import Map
from team import Team
import pygame

FPS = 60

class Game:
    def __init__(self, list_teams):
        self.map = Map()
        self.teams = [Team(name) for name in list_teams]
        self.selected_character = None
        self.turn = 0

    def run(self):
        pygame.init()
        pygame.display.set_caption("SUPER GAME")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    self.map.generate_character(self.teams, click_x, click_y)
                    if event.button == 1:  # Left Click
                        self.left_click(event.pos, self.turn)
                    elif event.button == 3:  # Right Click
                        self.right_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.change_turn()

            pygame.display.set_caption(self.teams[self.turn].get_name())    
            self.map.draw()
            clock.tick(FPS)
        
        pygame.quit()

    def left_click(self, click_pos, turn):
        x_tile, y_tile = self.map.get_tile(click_pos[0], click_pos[1])
<<<<<<< HEAD
        clicked_character = self.map.tiles[x_tile][y_tile].get_character()
        if clicked_character is not None and clicked_character.get_team() == self.teams[turn]:
            self.selected_character = clicked_character
        print(self.selected_character)
=======
        self.selected_character = self.map.tiles[x_tile][y_tile].get_character()
>>>>>>> d39052d (deux couleurs de joueurs)

    def right_click(self, click_pos):
        x_tile, y_tile = self.map.get_tile(click_pos[0], click_pos[1])
        if self.selected_character is not None:
            self.selected_character.move_tile(self.map.tiles[x_tile][y_tile])
    
    def change_turn(self):
        self.selected_character = None
        self.turn = (self.turn+1) % len(self.teams)
