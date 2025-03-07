from game import Game
from home_page import HomePage
from end_page import EndPage
from config import TEAMS, FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from utils import Font

import pygame
import sys

class SceneGestion:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() 

        pygame.mixer.music.load("musique.mp3")
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("super game !")

        self.home_page = HomePage(self.screen)
        self.current_scene = self.home_page

        Font.load()
    
    def run(self):
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
        if change == "game":
            self.current_scene = Game(TEAMS, self.screen)
        elif change == "Red":
            self.current_scene = EndPage(self.screen, "Red")
        elif change == "Blue":
            self.current_scene = EndPage(self.screen, "Blue")
        elif change == "home":
            self.current_scene = self.home_page