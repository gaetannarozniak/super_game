# to see the class dependencies structure
# pip install pyreverse
# pyreverse -o png ../super_game .
# the result is in the packages.png file

from game import Game
from config import TEAMS  
import pygame
import sys  


if __name__ == "__main__":
    game = Game(TEAMS)
    try:
        game.run()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
    # Ce bloc est toujours exécuté, même si une erreur se produit
        print("Fermeture propre de Pygame...")
        pygame.quit()
        sys.exit()  # Facultatif mais propre