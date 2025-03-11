import numpy as np
from game.team import Team
from game.map import Map
from .game_rl import GameRL
from abc import ABC

print("jeu")

class Env:

    def __init__(self):
        self.game = GameRL() 
        self.action_types = self.game.get_action_types_names()
        self.n_action_types = len(self.action_types)
        self.map_dimensions = self.game.get_map_dimensions()
        
    def get_game_obs(self):
        map:Map = self.game.get_map()
        teams = self.game.get_teams()
        selected_character = self.game.get_selected_character()
        obs = {}

        obs["team_lives"] = np.array([team.get_life() for team in teams])
        obs["team_gold"] =  np.array([team.get_gold() for team in teams])

        tiles = map.get_tile_array()  
        obs["map"] = np.array([[tile.get_rl_id()+[0] for  tile in row] for row in tiles])
        if selected_character is not None:
            i, j = selected_character.get_coordinates()
            obs["map"][i][j][-1] = 1

        return obs




    def reset(self):
        pass

    def step(self, action):
        pass 

