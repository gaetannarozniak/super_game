import pygame
from abc import abstractmethod, ABC
from config import TILE_SIZE

class Entity(ABC): # cannot instantiate abstract class Entity
    def __init__(self, tile, team):
        self.tile = tile
        self.team = team

        self.tile.set_entity(self)
        self.team.add_entity(self)

    @abstractmethod
    def draw(self, figure, x, y):
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
        self.tile.remove_entity() 
        future_tile.set_entity(self)
        self.tile = future_tile
        self.moved = True


class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=5)

    def draw(self, figure, x, y):
        tile_size = TILE_SIZE
        if self.team.name == "Red":
            pygame.draw.circle(figure, (255, 0, 0), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)
        elif self.team.name == "Blue":
            pygame.draw.circle(figure, (0, 0, 255), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)

    
class Base(Entity):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team)

    def draw(self, figure, x, y):
        base_image = pygame.image.load("images/base.png")
        base_image_scaled = pygame.transform.scale(base_image, (TILE_SIZE, TILE_SIZE))
        figure.blit(base_image_scaled, (x*TILE_SIZE, y*TILE_SIZE)) 
