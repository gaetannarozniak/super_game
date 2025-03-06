from terrains import Terrain
from characters import Character, Miner
import pygame
import random
from config import N_TILES_X, N_TILES_Y, TILE_SIZE 

class Tile:
    def __init__(self, x, y, terrain:Terrain = Terrain("grass"), character:Character=None):
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

    def draw(self, screen, accessible=False):
        self.terrain.draw(screen, self.x, self.y, accessible)
        if self.character is not None:
            self.character.draw(screen, self.x, self.y)

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
        self.nb_gold = (N_TILES_X * N_TILES_Y) // 10
        self.tiles = self.generate_map()
    
    def generate_map(self, distance_base=4, group_sizes=[2,3]):
        # generate the map, 
        # distance_base is the minimum distance between the bases and the golds,
        # group_sizes is the number of golds in a group
        tiles_type = [["grass" for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 
        tiles_type[1][1] = "base"
        tiles_type[-2][-2] = "base"
        
        golds = 0
        while golds < self.nb_gold:
            x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
            if tiles_type[x][y] != "grass":
                continue  
            
            #not too close to the bases
            if abs(x - 1) + abs(y - 1) <= distance_base or abs(x - N_TILES_X + 2) + abs(y - N_TILES_Y + 2) <= distance_base:
                continue
            
            group_size = random.choice(group_sizes)
            positions = [(x, y)]

            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            random.shuffle(directions)  
            
            for dx, dy in directions:
                if len(positions) >= group_size:
                    break
                nx, ny = x + dx, y + dy
                if 0 <= nx < N_TILES_X and 0 <= ny < N_TILES_Y and tiles_type[nx][ny] == "grass":
                    positions.append((nx, ny))

            if len(positions) == group_size:
                for px, py in positions:
                    tiles_type[px][py] = "gold"
                    golds += 1

        return [[Tile(x,y,Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 
        
    def draw(self, screen, selected_character):
        speed = selected_character.get_speed() if selected_character is not None else 0
        accessible_tiles = []
        if selected_character is not None:
            for x in range(N_TILES_X):
                for y in range(N_TILES_Y):
                    if self.tiles[x][y].get_character() is None and selected_character.tile.tile_dist(self.tiles[x][y]) <= speed:
                        accessible_tiles.append((x, y))

        for x in range(N_TILES_X):
            for y in range(N_TILES_Y):
                self.tiles[x][y].draw(screen, (x, y) in accessible_tiles) 

    def get_tile(self, click_x, click_y):
        return click_x // TILE_SIZE, click_y // TILE_SIZE
    
    def generate_character(self, teams, click_x, click_y):
        clicked_tile_x, clicked_tile_y = self.get_tile(click_x, click_y)
        if (clicked_tile_x, clicked_tile_y) == (1, 1):
            x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
            if self.tiles[x][y].get_character() is not None:
                return
            self.tiles[x][y].set_character(Miner(self.tiles[x][y], teams[0]))
            teams[0].add_character(self.tiles[x][y].get_character())
            teams[0].gold -= 100

        elif (clicked_tile_x, clicked_tile_y) == (N_TILES_X-2, N_TILES_Y-2):
            x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
            if self.tiles[x][y].get_character() is not None:
                return
            self.tiles[x][y].set_character(Miner(self.tiles[x][y], teams[1]))
            teams[1].add_character(self.tiles[x][y].get_character())
            teams[1].gold -= 100