import pygame
from abc import abstractmethod, ABC
from config import TILE_SIZE

class Entity(ABC): # cannot instantiate abstract class Entity
    def __init__(self, tile, team):
        self.tile = tile
        self.team = team

        self.tile.set_character(self)
        self.team.add_character(self)

    @abstractmethod
    def draw(self, screen, x, y):
        pass

    def get_team(self):
        return self.team

    def get_tile(self):
        return self.tile
    
    def get_speed(self):
        return self.speed


class Character(Entity, ABC):
    def __init__(self, tile, team, speed):
        super().__init__(tile, team)
        self.speed = speed
        self.moved = False

    def move_tile(self, future_tile):
        if self.tile.tile_dist(future_tile) > self.speed:
            return ValueError(f"impossible to move: the two tiles are too far away {self.speed} < {self.tile.tile_dist(future_tile)}")
        self.tile.remove_character() 
        future_tile.set_character(self)
        self.tile = future_tile
        self.moved = True


class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=5)

    def draw(self, screen, x, y):
        tile_size = TILE_SIZE
        if self.team.name == "Red":
            pygame.draw.circle(screen, (255, 0, 0), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)
        elif self.team.name == "Blue":
            pygame.draw.circle(screen, (0, 0, 255), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)

    