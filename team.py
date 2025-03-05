class Team:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        if character in self.characters:
            return ValueError("the character we want to add to the team is already in the team")
        self.characters.append(character)

    def remove_character(self, character):
        if character not in self.characters:
            return ValueError("the character we want to remove from the team is not in the team")
        self.characters.remove(character)

