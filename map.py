from terrains import Terrain
from math import abs
import pygame
import random

TILE_SIZE = 40
N_TILES_X, N_TILES_Y = 30, 20

class Tile:
    def __init__(self, x, y, screen, terrain:Terrain = Terrain("GRASS"), character=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.character = character
        self.terrain = terrain

        self.images = {
            "GRASS": pygame.image.load("images/grass.png"),
            "BASE": pygame.image.load("images/base.png"),
            "GOLD": pygame.image.load("images/gold.png")
        }

        for key in self.images:
            self.images[key] = pygame.transform.scale(self.images[key], (TILE_SIZE, TILE_SIZE))


    def draw(self):
        self.screen.blit(self.images["GRASS"], (self.x * TILE_SIZE, self.y * TILE_SIZE))
        if self.terrain.get_terrain_type() != "GRASS":
            self.screen.blit(self.images[self.terrain.get_terrain_type()], (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def get_terrain(self):
        return self.terrain
    
    def set_terrain(self, terrain):
        self.terrain = terrain
    
    def get_character(self):
        return self.character
    
    def set_character(self, character):
        self.character = character

    def remove_character(self):
        if self.character is None:
            raise ValueError(f"there is no character to remove in the tile ({self.x}, {self.y})")
        self.character = None

    def add_character(self, character):
        if self.character is not None:
            raise ValueError(f"there is already a character in the tile ({self.x}, {self.y})")
        self.character = character

    def tile_dist(self, other_tile):
        return abs(self.x - other_tile.x) + abs(self.y - other_tile.y)

class Map:
    def __init__(self):
        self.screen = pygame.display.set_mode((N_TILES_X * TILE_SIZE, N_TILES_Y * TILE_SIZE))
        tiles_type = [["GRASS" for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 
        self.nb_base = 2
        self.nb_gold = (N_TILES_X * N_TILES_Y) // 10 

        bases = 0
        while bases < self.nb_base:
            x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
            if tiles_type[x][y] == "GRASS":
                tiles_type[x][y] = "BASE"
                bases += 1
        
        golds = 0
        while golds < self.nb_gold:
            x, y = random.randint(0, N_TILES_X-1), random.randint(0, N_TILES_Y-1)
            if tiles_type[x][y] == "GRASS":
                tiles_type[x][y] = "GOLD"
                golds += 1

        self.tiles = [[Tile(x,y,self.screen,Terrain(tiles_type[x][y])) for y in range(N_TILES_Y)] for x in range(N_TILES_X)] 

    def draw(self):
        self.screen.fill((0,0,0))
        for x in range(N_TILES_X):
            for y in range(N_TILES_Y):
                self.tiles[x][y].draw() 
        pygame.display.flip()   

    def get_tile(self, click_x, click_y):
        return click_x // TILE_SIZE, click_y // TILE_SIZE