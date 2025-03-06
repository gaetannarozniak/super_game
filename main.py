# to see the class dependencies structure
# pip install pyreverse
# pyreverse -o png ../super_game .
# the result is in the packages.png file

from game import Game
from config import TEAMS    


if __name__ == "__main__":
    game = Game(TEAMS)
    game.run()