from config import MENU_WIDTH

class Menu:
    def __init__(self):
        self.color = (100, 100, 100)

    def display(self, screen, font, team):
        screen.fill(self.color)
        gold_text = font.render(f"Gold: {team.get_gold()}, Nb_characters: {len(team.characters)}", True, (0, 0, 0))
        screen.blit(gold_text, (10, 10))  # Position en haut à gauche
        screen.blit(font.render("Menu", True, (0,0,0)), (MENU_WIDTH // 2 - 36, 50))