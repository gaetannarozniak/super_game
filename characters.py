import pygame

class Character:
    def __init__(self, name, tile, team, speed:int):
        self.name = name
        self.tile = tile
        self.speed = speed
        self.team = team
        self.moved = False

    def move_tile(self, future_tile):
        if self.tile.tile_dist(future_tile) > self.speed:
            return ValueError(f"impossible to move: the two tiles are too far away {self.speed} < {self.tile.tile_dist(future_tile)}")
        self.tile.remove_character() 
        future_tile.set_character(self)
        self.tile = future_tile
        self.moved = True

    def draw(self, screen, x, y, parameters):
        tile_size = parameters.get_tile_size()
        if self.team.name == "Red":
            pygame.draw.circle(screen, (255, 0, 0), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)
        elif self.team.name == "Blue":
            pygame.draw.circle(screen, (0, 0, 255), (x * tile_size + tile_size // 2, y * tile_size + tile_size // 2), tile_size // 3)

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team
    
    def get_speed(self):
        return self.speed

class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(name = "miner", tile=tile, team=team, speed=5)


    