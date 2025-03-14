from .utils import Button, Font
from .config import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame

class EndPage:
    def __init__(self, winner):
        self.winner = winner
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "home", "Play Again ? ")
        self.background = pygame.image.load("game/resources/images/home_page.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.rect.collidepoint(event.pos):
                return self.button.callback()
        return None
    
    def display(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(Font.render(f"Team {self.winner} won ! ", "large"), (SCREEN_WIDTH//2 - 100, 100))
        self.button.draw(screen, "medium")
        pygame.display.flip()