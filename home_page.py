from utils import Button, Font, load_images
from config import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame

DUCK_IMAGES = load_images("background", ["duck_1", "duck_2", "duck_3"])

class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "game", "Start")
        self.background = pygame.image.load("images/home_page.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.time = 0
        self.current_image = 1
        self.duration_image = 6

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.rect.collidepoint(event.pos):
                return self.button.callback()
        return False
    
    def update_image(self):
        self.time += 1
        self.current_image = (self.time//self.duration_image) % 3 + 1
    
    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(DUCK_IMAGES[f"duck_{self.current_image}"], (SCREEN_WIDTH - 100, 100))
        self.update_image()

        self.screen.blit(Font.render("Welcome to super game", "large"), (SCREEN_WIDTH//2 - 140, 100))
        self.button.draw(self.screen, "medium")
        pygame.display.flip()


        
        