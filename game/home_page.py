from .utils import Button, Font, load_images
from .config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

import pygame
import random

# Centralisation des images
class Assets:
    DUCK_IMAGES = [load_images("background", [f"duck_{i}"], size_x=60, size_y=60)[f"duck_{i}"] for i in range(1, 4)]
    MINER_IMAGES = [load_images("background", [f"miner_{i}"], size_x=100, size_y=100)[f"miner_{i}"] for i in range(1, 4)]
    SOLDIER_IMAGES = [load_images("background", [f"soldier_{i}"], size_x=100, size_y=100)[f"soldier_{i}"] for i in range(1, 4)]
    BACKGROUND = pygame.transform.scale(
        pygame.image.load("game/resources/images/home_page.jpg"), 
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

# Classe générique pour les personnages animés
class Character:
    def __init__(self, images, x_range, y_range, speed_range):
        self.images = images
        self.x = SCREEN_WIDTH + random.randint(*x_range)
        self.y = random.randint(*y_range)
        self.speed = random.randint(*speed_range)
        self.time = random.randint(0, 10)
        self.current_frame = random.randint(0, len(images) - 1)
        self.speed_range = speed_range
        self.x_range = x_range

    def update(self, duration):
        self.time += 1
        self.current_frame = (self.time // duration) % len(self.images)
        self.x -= self.speed

        # Réapparition après sortie de l'écran
        if self.x < -100:
            self.x = SCREEN_WIDTH + random.randint(*self.x_range)
            self.time = 0
            self.speed = random.randint(*self.speed_range)  # Peut être ajusté dynamiquement

    def draw(self, screen):
        screen.blit(self.images[self.current_frame], (self.x, self.y))

# Classe pour la page d'accueil
class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "game", "Start")
        self.duration_image = FPS // 10

        height = SCREEN_HEIGHT * 550 // 800

        # Création des personnages avec des paramètres dynamiques
        self.characters = [
            *[Character(Assets.DUCK_IMAGES, (50, 1000), (50, 200), (7, 9)) for _ in range(6)],
            *[Character(Assets.MINER_IMAGES, (50, 1000), (height, height), (8, 11)) for _ in range(4)],
            *[Character(Assets.SOLDIER_IMAGES, (50, 1000), (height, height), (12, 15)) for _ in range(2)]
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.button.rect.collidepoint(event.pos):
            return self.button.callback()
        return False

    def update(self):
        for character in self.characters:
            character.update(self.duration_image)

    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(Assets.BACKGROUND, (0, 0))

        self.update()
        for character in self.characters:
            character.draw(self.screen)

        # Affichage du texte et des boutons
        self.screen.blit(Font.render("Welcome to super game", "large", color=(255, 255, 255)), (SCREEN_WIDTH//2 - 200, 100))
        self.button.draw(self.screen, "medium")

        pygame.display.flip()