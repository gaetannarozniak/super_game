from game.config import MAP_HEIGHT, MAP_WIDTH, FPS
from .env_rl import Env
from .agent import RandomAgent
import pygame

class RunAgents:
    def __init__(self, agent_1, agent_2):
        env = Env
        self.agent_1 = RandomAgent(0, env)
        self.agent_2 = agent_2
        screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))

        pygame.init()
        pygame.display.set_caption("Game")
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        turn = 0
        while running:
            self.game.display()
            if turn == 0:
                action = self.agent_1.get_action(self.game.get_obs)
            else:
                action = self.agent_2.get_action(self.game)
            self.game.handle_action(*action)
            turn = (turn+1) % 2
            clock.tick(FPS)