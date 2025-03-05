from map import Position

class Character:
    def __init__(self, name, pos: Position):
        self.name = name
        self.pos = pos

class Miner(Character):
    def __init__(self, name, pos: Position):
        super().__init__(name, pos)
        self.gold = 0

    def mine_gold(self):
        self.gold += 1

    def get_gold(self):
        return self.gold

    