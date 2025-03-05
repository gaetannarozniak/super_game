import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame classic loop")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Update game logic here
    # ...

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()