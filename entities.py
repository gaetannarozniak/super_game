import pygame
from abc import abstractmethod, ABC
from config import TILE_SIZE, CHARACTERS, BUILDINGS
from utils import load_images

CHARACTER_IMAGES = load_images("character", CHARACTERS)
BUILDING_IMAGES = load_images("building", BUILDINGS)

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
    
    @abstractmethod
    def die(self):
        pass

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
        print(f"character moved from ({self.tile.x}, {self.tile.y}) to ({future_tile.x}, {future_tile.y})")
        self.interact(future_tile)
        self.tile = future_tile
        self.moved = True
    
    def get_speed(self):
        return self.speed
    
    @abstractmethod
    def interact(self, tile):
        pass

    def die(self):
        if self.tile.get_character() != None:
            self.tile.remove_character()
        self.team.remove_entity(self)
        del self

    @abstractmethod
    def can_walk_on(self, other: Entity):
        pass

class Building(Entity, ABC):
    def __init__(self, tile, team, life):
        super().__init__(tile, team)
        self.tile.set_building(self)
        self.team.add_entity(self)
        self.life = life

    def get_life(self):
        return self.life
    
    def lose_life(self):
        self.life -= 1
        if self.life == 0:
            self.die()

    def die(self):
        self.tile.remove_building()
        self.team.remove_entity(self)
        del self

class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=10)

    def draw(self, figure, x, y):
        if self.team.get_name() == "Red":
            figure.blit(CHARACTER_IMAGES["miner_red"], (x * TILE_SIZE, y * TILE_SIZE))
        elif self.team.get_name() == "Blue":
            figure.blit(CHARACTER_IMAGES["miner_blue"], (x * TILE_SIZE, y * TILE_SIZE))
    
    def interact(self, tile):
        if tile.get_terrain_type() == "gold":
            tile.set_terrain_type("grass")
            self.team.add_gold(100)
        tile.set_character(self)

    def can_walk_on(self, other: Entity):
        if isinstance(other, Character):
            return False
        if isinstance(other, Building):
            return other.get_team() == self.team
        return True

    

class Soldier(Character):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, speed=10)

    def draw(self, figure, x, y):
        if self.team.get_name() == "Red":
            figure.blit(CHARACTER_IMAGES["soldier_red"], (x * TILE_SIZE, y * TILE_SIZE))
        elif self.team.get_name() == "Blue":
            figure.blit(CHARACTER_IMAGES["soldier_blue"], (x * TILE_SIZE, y * TILE_SIZE))

    def interact(self, tile):
        character = tile.get_character()
        building = tile.get_building()
        
        if character is not None and character.get_team() != self.team:
            if isinstance(character, Soldier):
                character.die()
                self.die()
            else:
                character.die()
                tile.set_character(self)
                
        elif building is not None and building.get_team() != self.team:
            building.lose_life()
            self.die()

        else:
            tile.set_character(self)
            
    def can_walk_on(self, other: Entity):
        if isinstance(other, Character):
            return other.get_team() != self.team
        return True
    
class Base(Building):
    def __init__(self, tile, team):
        super().__init__(tile=tile, team=team, life=2)

    def draw(self, figure, x, y):
        if self.team.get_name() == "Red":
            figure.blit(BUILDING_IMAGES["base_red"], (x * TILE_SIZE, y * TILE_SIZE))
        elif self.team.get_name() == "Blue":
            figure.blit(BUILDING_IMAGES["base_blue"], (x * TILE_SIZE, y * TILE_SIZE))