import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (400, 300), 100)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()