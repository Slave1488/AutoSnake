import pygame
from model.snake import LEFT, RIGHT, UP, DOWN, DIRECTION_NONE

skip_frame = 15


class GameController:
    def __init__(self, game):
        self._game = game
        self._counter = 0

    def tick(self):
        self._update_snakes_direction()
        self._update_game()

    def _update_snakes_direction(self):
        target_xx, target_yy = pygame.mouse.get_pos()
        c_w, c_h = cell_size(self._game.width, self._game.height)
        target_x = target_xx // c_w
        target_y = target_yy // c_h
        pos_x, pos_y = self._game.snake.pos()
        target_x -= pos_x
        target_y -= pos_y
        direction_x, direction_y = map(sign, (target_x, target_y))
        if direction_x == 1:
            direction = RIGHT
        elif direction_x == -1:
            direction = LEFT
        elif direction_y == 1:
            direction = UP
        elif direction_y == -1:
            direction = DOWN
        else:
            direction = DIRECTION_NONE
        self._game.update_snakes_direction(direction)

    def _update_game(self):
        if self._counter == 0:
            self._game.step()
        self._update_counter()

    def _update_counter(self):
        self._counter += 1
        if self._counter == skip_frame:
            self._counter = 0


def cell_size(width, height):
    w, h = pygame.display.get_surface().get_size()
    return w / width, h / height


def sign(num):
    return -1 if num < 0 else 1 if num > 0 else 0
