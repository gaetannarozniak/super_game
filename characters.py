from map import Tile

class Character:
    def __init__(self, name, pos: Tile):
        self.name = name
        self.pos = pos

class Miner(Character):
    def __init__(self, name, pos: Tile):
        super().__init__(name, pos)
        self.gold = 0

    def mine_gold(self):
        self.gold += 1

    def get_gold(self):
        return self.gold

    