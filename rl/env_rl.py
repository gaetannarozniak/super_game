from game.game_rl import GameRL
from abc import ABC

print("jeu")

class Env:

    def __init__(self):
        self.game = GameRL() 
        self.action_types = self.game.get_action_types_names()
        self.n_action_types = len(self.action_types)
        self.map_dimensions = self.game.get_map_dimensions()
        

    def compute_tile_id(tile):


    def get_game_obs(self):
        map = self.game.get_map()
        teams = self.game.get_teams()




    def reset(self):
        pass

    def step(self, action):
        pass 

