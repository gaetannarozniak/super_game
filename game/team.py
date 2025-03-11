from .entities import Base, Character
from .config import TEAMS

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
        if current_character not in moveable_characters:
            return moveable_characters[0]
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

    def buy_character(self, unit_class: Character):
        if not issubclass(unit_class, Character):
            raise TypeError("impossible to buy {unit_class} character")
        if not self.base.is_empty():
            print("there is already a character on the base")
            return None
        if self.gold >= unit_class.gold_cost:
            self.gold -= unit_class.gold_cost
            return unit_class(self.base.get_tile(), team=self)
        return None

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
    
    def set_life(self, life):
        self.base.set_life(life)

    def get_nb_character(self):
        return len([e for e in self.entities if isinstance(e, Character)])

    def get_rl_id(self):
        return TEAMS.index(self.name)