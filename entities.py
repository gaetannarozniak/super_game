import pygame
from abc import abstractmethod, ABC
from config import TILE_SIZE

class Entity(ABC): # cannot instantiate abstract class Entity
    def __init__(self, tile, team):
        self.tile = tile
        self.team = team

    @abstractmethod
    def draw(self, figure, x, y):
        pass

    def get_team(self):
        return self.team

    def get_tile(self):
        return self.tile
    
    def die(self):
        self.tile.remove_character()
        self.team.remove_entity(self)
        del self


class Character(Entity, ABC):
    def __init__(self, tile, team, speed):
        super().__init__(tile, team)
        self.speed = speed
        self.moved = False
        self.tile.set_character(self)
        self.team.add_entity(self)

    def move_tile(self, future_tile):
        if self.tile.tile_dist(future_tile) > self.speed:
            return ValueError(f"impossible to move: the two tiles are too far away {self.speed} < {self.tile.tile_dist(future_tile)}")
        self.tile.remove_character() 
        self.interact(future_tile)
        future_tile.set_character(self)
        self.tile = future_tile
        self.moved = True
    
    def get_speed(self):
        return self.speed

class Building(Entity, ABC):
    def __init__(self, tile, team):
        super().__init__(tile, team)
        self.tile.set_building(self)
        self.team.add_entity(self)

class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=30)

    def draw(self, figure, x, y):
        tile_size = TILE_SIZE
        if self.team.name == "Red":
            pygame.draw.circle(figure, (255, 0, 0), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)
        elif self.team.name == "Blue":
            pygame.draw.circle(figure, (0, 0, 255), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)
    
    def interact(self, tile):
        if tile.get_terrain_type() == "gold":
            tile.set_terrain_type("grass")
            self.team.add_gold(100)

class Soldier(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=50)

    def draw(self, figure, x, y):
        tile_size = TILE_SIZE
        if self.team.name == "Red":
            pygame.draw.rect(figure, (255, 0, 0), (x * tile_size + tile_size // 4, y * tile_size + tile_size // 4, tile_size // 2, tile_size // 2))
        elif self.team.name == "Blue":
            pygame.draw.rect(figure, (0, 0, 255), (x * tile_size + tile_size // 4, y * tile_size + tile_size // 4, tile_size // 2, tile_size // 2))

    def interact(self, tile):
        character = tile.get_character()
        if character is not None and character.get_team() != self.team:
            if isinstance(character, Soldier):
                character.die()
                self.die()
            else:
                character.die()
            
    
class Base(Building):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team)

    def draw(self, figure, x, y):
        base_image = pygame.image.load("images/base.png")
        base_image_scaled = pygame.transform.scale(base_image, (TILE_SIZE, TILE_SIZE))
        figure.blit(base_image_scaled, (x*TILE_SIZE, y*TILE_SIZE))
