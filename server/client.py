from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, TEAMS
from game.utils import Font, Button
from game.game import Game

import pygame

class Client:
    def __init__(self, network):
        self.network = network
        self.player = self.network.get_player()
        self.seed = self.network.get_seed()
        print("You are player", self.player)

        self.background = pygame.image.load("game/resources/images/home_page.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, lambda: "home", "Leave Server")
        self.game = Game(TEAMS, self.seed)
        self.ready = False

    def update_game(self):
        try:
            if self.ready:
                if self.player != self.game.get_turn():
                    dict_event = self.network.send("connected")
                    if dict_event == "disconnected":
                        self.reset()
                    if isinstance(dict_event, dict):
                        event = self.dict_to_event(dict_event)
                        return self.game.handle_event(event)
            else:
                self.ready = self.network.send("waiting")
            return None
        except:
            print("Couldn't get game")
            return "home"

    def handle_event(self, event):
        try:
            if self.ready:
                if self.player == self.game.get_turn():
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        dict_event = self.event_to_dict(event)
                        self.ready = self.network.send(dict_event)
                        if not self.ready:
                            self.reset()
                        else:
                            return self.game.handle_event(event)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        return self.button.callback()
            return False
        except:
            print("Couldn't get game")
            return "home"
    
    def display(self, screen):
        if not self.ready: 
            screen.blit(self.background, (0, 0))
            screen.blit(Font.render("Waiting for player two", "large", color=(255, 255, 255)), (SCREEN_WIDTH//2 - 200, 100))
            self.button.draw(screen, "medium")
            pygame.display.flip()
        else:
            self.game.display(screen, display_menu=(self.player == self.game.get_turn()))

    def event_to_dict(self, event):
        return {"type": event.type, **event.dict}

    def dict_to_event(self, event_dict):
        return pygame.event.Event(event_dict["type"], **{k: v for k, v in event_dict.items() if k != "type"})
    
    def reset(self):
        self.game = Game(TEAMS, self.seed)
        self.ready = False
            