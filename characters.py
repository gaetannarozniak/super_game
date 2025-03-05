from map import Tile

class Character:
    def __init__(self, name, tile: Tile, speed:int, team):
        self.name = name
        self.tile = tile
        self.speed = speed
        self.team = team 

    def move_tile(self, future_tile):
        if self.tile.tile_dist(future_tile) > self.speed:
            return ValueError(f"impossible to move: the two tiles are too far away {self.speed = } < {self.tile_dist(future_tile)}")
        self.tile.remove_character() 
        future_tile.set_character(self)

class Miner(Character):
    def __init__(self, name, tile: Tile):
        super().__init__(name, tile, speed=2)


    