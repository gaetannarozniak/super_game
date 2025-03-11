FPS: int = 20
DISPLAY_TILE_IDS = False

TEAMS = ["Red", "Blue"]
TERRAINS = ["grass", "gold", "tree"]
CHARACTERS = ["miner_red", "miner_blue", "soldier_red", "soldier_blue"] # for images loading
BUILDINGS = ["base_red", "base_blue"] # for images loading

N_TILES_X = 20
N_TILES_Y = 20
BASE_COORDS = [(1, 1), (N_TILES_X-2, N_TILES_Y-2)]
TILE_SIZE = 40

MENU_WIDTH = 200
MAP_WIDTH = N_TILES_X * TILE_SIZE
MAP_HEIGHT = N_TILES_Y * TILE_SIZE
SCREEN_WIDTH = MAP_WIDTH + MENU_WIDTH
SCREEN_HEIGHT = MAP_HEIGHT

MIN_WINDOW_WIDTH = 400
 
MINER_SPEED: int = 5
SOLDIER_SPEED: int = 7