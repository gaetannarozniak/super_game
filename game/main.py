# to see the class dependencies structure
# pip install pyreverse
# pyreverse -o png ../super_game .
# the result is in the packages.png file

import pygame
import sys
import traceback  # Import the traceback module
from scene_gestion import SceneGestion

if __name__ == "__main__":
    scene_gestion = SceneGestion()
    try:
        scene_gestion.run()
    except Exception as e:
        print("Une erreur est survenue :")
        traceback.print_exc()  # This prints the full stack trace
    finally:
        print("Fermeture propre de Pygame...")
        pygame.quit()
        sys.exit()  # Facultatif mais propre
