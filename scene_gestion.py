from game import Game
#from home_page import HomePage
from config import TEAMS, FPS, SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import sys

class SceneGestion:
    def __init__(self):

        pygame.font.init()
        self.font = pygame.font.Font(None, 25)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("super game !")

        self.home_page = None
        self.game = Game(TEAMS, self.screen, self.font)
        self.current_scene = self.game
    
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    change = self.current_scene.handle_event(event)
                    self.change_scene(change)
            clock.tick(FPS)

    def change_scene(self, change):
        if change:
            if self.current_scene == self.home_page:
                self.current_scene = self.game
            else:
                self.current_scene = self.home_page
        