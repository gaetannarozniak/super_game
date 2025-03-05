from terrains import Terrain
import pygame
import random

TILE_SIZE = 40
N_TILES_X, N_TILES_Y = 30, 20

List_images = ["grass", "base", "gold"]
IMAGES = {key: pygame.image.load(f"images/{key}.png") for key in List_images}
for key in IMAGES:
    IMAGES[key] = pygame.transform.scale(IMAGES[key], (TILE_SIZE, TILE_SIZE))

class Tile:
    def __init__(self, x, y, screen, terrain:Terrain = Terrain("grass"), character=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

    def draw(self):
        self.screen.blit(IMAGES["grass"], (self.x * TILE_SIZE, self.y * TILE_SIZE))
        if self.terrain.get_terrain_type() != "grass":
            self.screen.blit(IMAGES[self.terrain.get_terrain_type()], (self.x * TILE_SIZE, self.y * TILE_SIZE))

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

    def set_character(self, character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.x}, {self.y})")
        self.character = character

    def tile_dist(self, other_tile):
        return abs(self.x - other_tile.x) + abs(self.y - other_tile.y)


class Map:
    def __init__(self):
        self.screen = pygame.display.set_mode((N_TILES_X * TILE_SIZE, N_TILES_Y * TILE_SIZE))
        self.nb_gold = (N_TILES_X * N_TILES_Y) // 20 
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

        return [[Tile(x,y,self.screen,Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 

    def left_click(self, click_pos):
        x_tile, y_tile = self.get_tile(click_pos[0], click_pos[1])
        self.selected_character = self.tiles[x_tile][y_tile].get_character()

    
    def right_click(self, click_pos):
        x_tile, y_tile = self.get_tile(click_pos[0], click_pos[1])
        if self.selected_character is not None:
            self.selected_character.move_tile(self.tiles[x_tile][y_tile])
        
    def draw(self):
        self.screen.fill((0,0,0))
        for x in range(N_TILES_X):
            for y in range(N_TILES_Y):
                self.tiles[x][y].draw() 
        pygame.display.flip()   

    def get_tile(self, click_x, click_y):
        return click_x // TILE_SIZE, click_y // TILE_SIZE