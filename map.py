from terrains import Terrain
from characters import Character, Miner
import pygame
import random
from parameters import Parameters

class Tile:
    def __init__(self, x, y, terrain:Terrain = Terrain("grass"), character:Character=None):
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

    def draw(self, screen, parameters, accessible=False):
        self.terrain.draw(screen, self.x, self.y, parameters, accessible)
        if self.character is not None:
            self.character.draw(screen, self.x, self.y, parameters)

    def get_terrain(self):
        return self.terrain
    
    def set_terrain(self, terrain):
        self.terrain = terrain
    
    def get_character(self):
        return self.character

    def remove_character(self):
        if self.character is None:
            raise ValueError(f"there is no character to remove in the tile ({self.x}, {self.y})")
        self.character = None

    def set_character(self, character:Character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.x}, {self.y})")
        self.character = character

    def tile_dist(self, other_tile):
        return abs(self.x - other_tile.x) + abs(self.y - other_tile.y)


class Map:
    def __init__(self):
        self.parameters = Parameters()
        self.screen = pygame.display.set_mode((self.parameters.get_n_tiles_x() * self.parameters.get_tile_size(), self.parameters.get_n_tiles_y() * self.parameters.get_tile_size()))
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.nb_gold = (self.parameters.get_n_tiles_x() * self.parameters.get_n_tiles_y()) // 10
        self.tiles = self.generate_map()
    
    def generate_map(self, distance_base=4, group_sizes=[2,3]):
        # generate the map, 
        # distance_base is the minimum distance between the bases and the golds,
        # group_sizes is the number of golds in a group
        tiles_type = [["grass" for y in range(self.parameters.get_n_tiles_y())] for x in range(self.parameters.get_n_tiles_x())] 
        tiles_type[1][1] = "base"
        tiles_type[-2][-2] = "base"
        
        golds = 0
        while golds < self.nb_gold:
            x, y = random.randint(0, self.parameters.get_n_tiles_x()-1), random.randint(0, self.parameters.get_n_tiles_y()-1)
            if tiles_type[x][y] != "grass":
                continue  
            
            #not too close to the bases
            if abs(x - 1) + abs(y - 1) <= distance_base or abs(x - self.parameters.get_n_tiles_x() + 2) + abs(y - self.parameters.get_n_tiles_y() + 2) <= distance_base:
                continue
            
            group_size = random.choice(group_sizes)
            positions = [(x, y)]

            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            random.shuffle(directions)  
            
            for dx, dy in directions:
                if len(positions) >= group_size:
                    break
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.parameters.get_n_tiles_x() and 0 <= ny < self.parameters.get_n_tiles_y() and tiles_type[nx][ny] == "grass":
                    positions.append((nx, ny))

            if len(positions) == group_size:
                for px, py in positions:
                    tiles_type[px][py] = "gold"
                    golds += 1

        return [[Tile(x,y,Terrain(tiles_type[x][y])) for y in range(self.parameters.get_n_tiles_y())] for x in range(self.parameters.get_n_tiles_x())] 
        
    def draw(self, selected_character, team):
        speed = selected_character.get_speed() if selected_character is not None else 0
        accessible_tiles = []
        if selected_character is not None:
            for x in range(self.parameters.get_n_tiles_x()):
                for y in range(self.parameters.get_n_tiles_y()):
                    if self.tiles[x][y].get_character() is None and selected_character.tile.tile_dist(self.tiles[x][y]) <= speed:
                        accessible_tiles.append((x, y))

        self.screen.fill((255,255,255))
        for x in range(self.parameters.get_n_tiles_x()):
            for y in range(self.parameters.get_n_tiles_y()):
                self.tiles[x][y].draw(self.screen, self.parameters, (x, y) in accessible_tiles)
        gold_text = self.font.render(f"Gold: {team.get_gold()}, Nb_characters: {len(team.characters)}", True, (0, 0, 0))
        self.screen.blit(gold_text, (10, 10))  # Position en haut à gauche

        pygame.display.flip()   

    def get_tile(self, click_x, click_y):
        return click_x // self.parameters.get_tile_size(), click_y // self.parameters.get_tile_size()
    
    def generate_character(self, teams, click_x, click_y):
        clicked_tile_x, clicked_tile_y = self.get_tile(click_x, click_y)
        if (clicked_tile_x, clicked_tile_y) == (1, 1):
            x, y = random.randint(0, self.parameters.get_n_tiles_x()-1), random.randint(0, self.parameters.get_n_tiles_y()-1)
            if self.tiles[x][y].get_character() is not None:
                return
            self.tiles[x][y].set_character(Miner(self.tiles[x][y], teams[0]))
            teams[0].add_character(self.tiles[x][y].get_character())
            teams[0].gold -= 100

        elif (clicked_tile_x, clicked_tile_y) == (self.parameters.get_n_tiles_x()-2, self.parameters.get_n_tiles_y()-2):
            x, y = random.randint(0, self.parameters.get_n_tiles_x()-1), random.randint(0, self.parameters.get_n_tiles_y()-1)
            if self.tiles[x][y].get_character() is not None:
                return
            self.tiles[x][y].set_character(Miner(self.tiles[x][y], teams[1]))
            teams[1].add_character(self.tiles[x][y].get_character())
            teams[1].gold -= 100

    def modify_window_size(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        WINDOW_WIDTH = max(WINDOW_WIDTH, self.parameters.get_min_window_width())
        WINDOW_HEIGHT = max(WINDOW_HEIGHT, self.parameters.get_min_window_height())
        tile_size = min(WINDOW_WIDTH // self.parameters.get_n_tiles_x(), WINDOW_HEIGHT // self.parameters.get_n_tiles_y())
        self.parameters.set_tile_size(tile_size)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))