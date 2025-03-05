import pygame

TILE_SIZE = 40

class Character:
    def __init__(self, name, tile, team, speed:int):
        self.name = name
        self.tile = tile
        self.speed = speed
        self.team = team 

    def move_tile(self, future_tile):
        if self.tile.tile_dist(future_tile) > self.speed:
            return ValueError(f"impossible to move: the two tiles are too far away {self.speed = } < {self.tile_dist(future_tile)}")
        self.tile.remove_character() 
        future_tile.set_character(self)
        self.tile = future_tile

    def draw(self, screen, x, y):
        if self.team.name == "Red":
            pygame.draw.circle(screen, (255, 0, 0), (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)
        elif self.team.name == "Blue":
            pygame.draw.circle(screen, (0, 0, 255), (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

class Miner(Character):
    def __init__(self, tile, team):
        super().__init__(name = "miner", tile=tile, team=team, speed=5)


    