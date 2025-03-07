from utils import Button, Font
from config import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame

class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: True, "Start")
        self.background = pygame.image.load("images/home_page.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.rect.collidepoint(event.pos):
                return self.button.callback()
        self.display()
        return False
    
    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(Font.render("Welcome to super game", "large"), (SCREEN_WIDTH//2 - 140, 100))
        self.button.draw(self.screen, "medium")
        pygame.display.flip()
        
        