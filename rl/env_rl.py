from typing import Any
import numpy as np
from game.entities import Character
from game.team import Team
from game.map import Map
from .game_rl import GameRL
from abc import ABC

print("jeu")

class Reward:
    gold_reward = 0.01
    life_reward = 10 

    def __init__(self, n_teams: int):
        self.n_teams = n_teams

    def team_reward(self, obs: Obs, team_id: int):
        r = 0
        r += obs.team_gold(team_id) * self.gold_reward
        r += obs.team_lives(team_id) * self.life_reward
        for c in obs.team_characters:
            r += c.gold_cost() * self.gold_reward
        return r

    def __call__(self, obs: Obs, team_id: int):
        r = 0
        for i in range(self.n_teams):
            if i==team_id:
                r += self.team_reward(obs, i)
            else:
                r -= self.team_reward(obs, i)
        return r


class Obs:

    def __init__(self, map, teams, selected_character):
        self.obs = {}
        self.teams = teams

        self.obs["team_lives"] = np.array([team.get_life() for team in teams])
        self.obs["team_gold"] =  np.array([team.get_gold() for team in teams])

        tiles = map.get_tile_array()  
        self.obs["map"] = np.array([[tile.get_rl_id()+[0] for  tile in row] for row in tiles])
        if selected_character is not None:
            i, j = selected_character.get_coordinates()
            self.obs["map"][i][j][-1] = 1

    def team_lives(self, team_id):
        return self.obs["team_lives"][team_id]

    def team_gold(self, team_id):
        return self.obs["team_gold"][team_id]

    def team_characters(self, team_id):
        return [c for c in self.teams[team_id].get_entities if isinstance(c, Character)]

    def __call__(self):
        return self.obs

class Env:

    def __init__(self, team_id):
        self.team_id = team_id
        self.reward_model = Reward(n_teams=len(self.game.get_teams()))
        self.game = GameRL() 
        self.action_types = self.game.get_action_types_names()
        self.n_action_types = len(self.action_types)
        self.map_dimensions = self.game.get_map_dimensions()
        
    def get_game_obs(self):
        map:Map = self.game.get_map()
        teams = self.game.get_teams()
        selected_character = self.game.get_selected_character()
        return Obs(map, teams, selected_character)


    def reset(self):
        pass

    def step(self, action):
        obs = self.get_game_obs()
        reward = self.compute_reward(obs)
        pass 

