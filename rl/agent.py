from .env_rl import Env
from numpy import random

class RandomAgent:

    def __init__(self, team_id: int, env: Env):
        self.team_id = team_id
        self.env = env
        self.n_action_types = env.get_n_actions()
        self.map_dimensions = env.get_map_dimensions()

    def choose_action(self):
        action_type = random.randint(0, self.n_action_types)
        ni, nj = self.map_dimensions
        action_tile_i = random.randint(0, ni)
        action_tile_j = random.randint(0, nj)
        action = {
            "type": action_type,
            "movement_tile": (action_tile_i, action_tile_j)
        }
        return action
