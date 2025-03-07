from utils import Button, Font, load_images
from config import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import random

DUCK_IMAGES = load_images("background", ["duck_1", "duck_2", "duck_3"], size_x=60, size_y=60)
MINER_IMAGES = load_images("background", ["miner_1", "miner_2", "miner_3"], size_x=100, size_y=100)
SOLDIER_IMAGES = load_images("background", ["soldier_1", "soldier_2", "soldier_3"], size_x=100, size_y=100)

class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "game", "Start")
        self.background = pygame.image.load("resources/images/home_page.jpg")
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

        self.number_miners = 4
        self.miners = []
        for _ in range(self.number_miners):
            miner = {
                "current_image": random.randint(1, 3), 
                "miner_x": SCREEN_WIDTH + random.randint(50, 2000), 
                "miner_y": 400, 
                "miner_speed": random.randint(3, 5),
                "time": random.randint(0, 10),
            }
            self.miners.append(miner)

        self.number_soldiers = 2
        self.soldiers = []
        for _ in range(self.number_soldiers):
            soldier = {
                "current_image": random.randint(1, 3), 
                "soldier_x": SCREEN_WIDTH + random.randint(50, 2000), 
                "soldier_y": 400, 
                "soldier_speed": random.randint(6, 7),
                "time": random.randint(0, 10),
            }
            self.soldiers.append(soldier)

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
                duck["duck_speed"] = random.randint(3, 5)

    def update_miner(self):
        for miner in self.miners:
            miner["time"] += 1
            miner["current_image"] = (miner["time"] // self.duration_image) % 3 + 1
            miner["miner_x"] -= miner["miner_speed"]
            
            if miner["miner_x"] < -100:
                miner["miner_x"] = SCREEN_WIDTH + random.randint(50, 200)
                miner["time"] = 0
                miner["miner_speed"] = random.randint(3, 5)

    def update_soldier(self):
        for soldier in self.soldiers:
            soldier["time"] += 1
            soldier["current_image"] = (soldier["time"] // self.duration_image) % 3 + 1
            soldier["soldier_x"] -= soldier["soldier_speed"]
            
            if soldier["soldier_x"] < -100:
                soldier["soldier_x"] = SCREEN_WIDTH + random.randint(1500, 2000)
                soldier["time"] = 0
                soldier["soldier_speed"] = random.randint(5, 7)
    
    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (0, 0))

        self.update_ducks()
        for duck in self.ducks:
            self.screen.blit(DUCK_IMAGES[f"duck_{duck['current_image']}"], (duck["duck_x"], duck["duck_y"]))

        self.update_miner()
        for miner in self.miners:
            self.screen.blit(MINER_IMAGES[f"miner_{miner['current_image']}"], (miner["miner_x"], miner["miner_y"]))

        self.update_soldier()
        for soldier in self.soldiers:
            self.screen.blit(SOLDIER_IMAGES[f"soldier_{soldier['current_image']}"], (soldier["soldier_x"], soldier["soldier_y"]))

        self.screen.blit(Font.render("Welcome to super game", "large", color=(255, 255, 255)), (SCREEN_WIDTH//2 - 200, 100))
        
        self.button.draw(self.screen, "medium")
        pygame.display.flip()


        
        