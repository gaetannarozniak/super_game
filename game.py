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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click
                    map.left_click(event.pos)
                elif event.button == 3:  # Right Click
                    map.right_click(event.pos)

        map.draw()
    
    pygame.quit()