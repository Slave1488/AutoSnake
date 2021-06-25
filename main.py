import pygame
from model.game import Game
from view.gameView import GameView
from controller.gameController import GameController

game = Game(9, 7)

pygame.init()

screen = pygame.display.set_mode((800, 600))

view = GameView(screen, game)

controller = GameController(game)

clock = pygame.time.Clock()
FPS = 30

running = True
while running:
    view.draw()
    controller.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)

pygame.quit()
