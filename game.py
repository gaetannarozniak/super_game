from map import Map
import pygame

def run():
    pygame.init()
    pygame.display.set_caption("SUPER GAME")
    map = Map()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Clic de souris
                click_x, click_y = event.pos
                x, y = map.get_tile(click_x, click_y)
                print(x,y)

        map.draw()
    
    pygame.quit()