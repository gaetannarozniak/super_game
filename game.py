from map import Map
from team import Team
import pygame

class Game:
    def __init__(self, n_teams):
        self.map = Map()
        self.teams = [Team() for _ in range(n_teams)]

    def run(self):
        pygame.init()
        pygame.display.set_caption("SUPER GAME")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left Click
                        self.map.left_click(event.pos)
                    elif event.button == 3:  # Right Click
                        self.map.right_click(event.pos)

            self.map.draw()
        
        pygame.quit()