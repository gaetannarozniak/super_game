# to see the class dependencies structure
# pip install pyreverse
# pyreverse -o png ../super_game .
# the result is in the packages.png file

import pygame
import sys  
from scene_gestion import SceneGestion


if __name__ == "__main__":
    scene_gestion = SceneGestion()
    try:
        scene_gestion.run()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
    # Ce bloc est toujours exécuté, même si une erreur se produit
        print("Fermeture propre de Pygame...")
        pygame.quit()
        sys.exit()  # Facultatif mais propre