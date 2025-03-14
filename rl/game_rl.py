from game.map import Map
from game.team import Team
from game.entities import Character, Miner, Soldier
from game.config import TEAMS
from .display_game_rl import DisplayGameRL
from .config_rl import PENALTY

class GameRL:
    def __init__(self, list_teams=TEAMS, screen=None):
        self.map = Map()
        self.teams = [Team(team_name) for team_name in TEAMS]
        self.selected_character = None
        self.turn = 0

        if screen is not None:
            self.display_game = DisplayGameRL(self.map, screen)

    def handle_action(self, action_type, action_tile):
        action_method = getattr(self, action_type, None)
        if callable(action_method):
            if action_method == self.move_character:
                return action_method(*action_tile)
            return action_method()
        else:
            raise ValueError(f"Action '{action_type}' not found")
        
    def display(self):
        self.display_game.display(self.selected_character, self.teams, self.turn)
        
    def buy_miner(self):
        new_miner = self.teams[self.turn].buy_character(Miner)
        selected_character = new_miner
        if selected_character is None:
            return PENALTY
        return 0
        
    def buy_soldier(self):
        new_soldier = self.teams[self.turn].buy_character(Soldier)
        selected_character = new_soldier
        if selected_character is None:
            return PENALTY
        return 0
        
    def change_turn(self):
        self.selected_character = None
        for entity in self.teams[self.turn].entities:
            if isinstance(entity, Character):
                entity.moved = False
        self.turn = (self.turn+1) % len(self.teams)
        self.select_next_character()
        return 0
    
    def move_character(self, i,j):
        tile = self.map.get_tile_ij(i,j)

        if self.selected_character is None:
            return PENALTY
        if not (tile in self.map.get_accessible_tiles(self.selected_character)):
            return PENALTY
        
        if self.selected_character.get_team() != self.teams[self.turn]:
            raise ValueError("Selected Character not in the good team !")
        if self.selected_character.moved:
            raise ValueError("Selected Character already moved !")
        
        self.selected_character.move_tile(tile)
        self.select_next_character()
        return 0
        
    def select_next_character(self):
        self.selected_character = self.teams[self.turn].get_next_character(self.selected_character)
        if self.selected_character is None or self.teams[self.turn].get_nb_character() == 0:
            return PENALTY
        return 0

    def get_map(self):
        return self.map
    
    def get_teams(self):
        return self.teams
    
    def get_selected_character(self):
        return self.selected_character
    
    def get_type_action_names(self):
        return["buy_miner", "buy_soldier", "change_turn", "select_next_character", "move_character"]

    def get_map_dimensions(self):
        return self.map.get_dimensions()
    

"""   
class RunAgents:
    def __init__(self, agent_1, agent_2):
        self.agent_1 = agent_1
        self.agent_2 = agent_2
        screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
        self.game = GameRL(screen = screen)

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
            clock.tick(FPS)"""