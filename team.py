from entities import Base

class Team:
    def __init__(self, name):
        self.entities = []
        self.name = name
        self.gold = 1000

    def add_entity(self, entity):
        if entity in self.entities:
            return ValueError("the entity we want to add to the team is already in the team")
        self.entities.append(entity)

    def remove_entity(self, entity):
        if entity not in self.entities:
            return ValueError("the entity we want to remove from the team is not in the team")
        self.entities.remove(entity)
        entity.set_team(None)

    def create_base(self, tile):
        Base(tile, self)

    def get_name(self):
        return self.name
    
    def get_gold(self):
        return self.gold