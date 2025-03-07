from utils import Button, Font, load_images
from config import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import random

DUCK_IMAGES = load_images("background", ["duck_1", "duck_2", "duck_3"])

class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "game", "Start")
        self.background = pygame.image.load("images/home_page.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.time = 0

        self.time = 0
        self.duration_image = 6
        self.num_ducks = 6
        self.ducks = []

        for _ in range(self.num_ducks):
            duck = {
                "current_image": random.randint(1, 3), 
                "duck_x": SCREEN_WIDTH + random.randint(50, 2000), 
                "duck_y": random.randint(50, 200), 
                "duck_speed": random.randint(3, 5),
                "time": random.randint(0, 10),
            }
            self.ducks.append(duck)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.rect.collidepoint(event.pos):
                return self.button.callback()
        return False
    
    def update_ducks(self):
        for duck in self.ducks:
            duck["time"] += 1
            duck["current_image"] = (duck["time"] // self.duration_image) % 3 + 1
            duck["duck_x"] -= duck["duck_speed"]
            
            if duck["duck_x"] < -100:
                duck["duck_x"] = SCREEN_WIDTH + random.randint(50, 200)
                duck["duck_y"] = random.randint(50, 200)
                duck["time"] = 0
    
    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (0, 0))

        self.update_ducks()
        for duck in self.ducks:
            self.screen.blit(DUCK_IMAGES[f"duck_{duck['current_image']}"], (duck["duck_x"], duck["duck_y"]))

        self.screen.blit(Font.render("Welcome to super game", "large"), (SCREEN_WIDTH//2 - 140, 100))
        self.button.draw(self.screen, "medium")
        pygame.display.flip()


        
        