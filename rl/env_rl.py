from game.game import Game

import pygame

screen = pygame.display.set_mode((800, 600))
list_teams = ["Red", "Blue"]
game = Game(list_teams, screen)

print("jeu")