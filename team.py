from entities import Base, Miner, Soldier, Character

class Team:
    def __init__(self, name, base_tile):
        self.entities = []
        self.name = name
        self.base = self.create_base(base_tile)
        self.gold = 20000

    def get_next_character(self, current_character: Character = None):
        moveable_characters = [e for e in self.entities if isinstance(e, Character) and not e.moved]
        if len(moveable_characters) == 0:
            print("There are no moveable characters in this team, impossible to select one")
            return None
        if current_character is None:
            return moveable_characters[0]
        if current_character not in moveable_characters:
            raise ValueError("The selected character is not in the team moveable characters")
        index = moveable_characters.index(current_character)
        return moveable_characters[(index+1) % len(moveable_characters)]
        

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

    def get_life(self):
        return self.base.get_life()