from entities import Base, Miner, Soldier

class Team:
    def __init__(self, name, base_tile):
        self.entities = []
        self.name = name
        self.base = self.create_base(base_tile)
        self.gold = 1000

    def add_entity(self, entity):
        if entity in self.entities:
            return ValueError("the entity we want to add to the team is already in the team")
        self.entities.append(entity)

    def remove_entity(self, entity):
        if entity not in self.entities:
            return ValueError("the entity we want to remove from the team is not in the team")
        self.entities.remove(entity)

    def buy_miner(self):
        if self.gold >= 100:
            self.gold -= 100
            Miner(self.base.tile, self)

    def buy_soldier(self):
        if self.gold >= 200:
            self.gold -= 200
            Soldier(self.base.tile, self)

    def create_base(self, tile):
        return Base(tile, self)

    def get_name(self):
        return self.name
    
    def get_gold(self):
        return self.gold
    
    def add_gold(self, gold):
        self.gold += gold