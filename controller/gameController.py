from model.game import Game
from model.snake import LEFT, RIGHT, UP, DOWN, DIRECTION_NONE
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint

skip_frame = 15


class GameController:
    def __init__(self, game: Game, w, h):
        self._game = game
        self.cell_size = lambda: (w / game.width, h / game.height)

    def tick(self):
        self._update_snakes_direction()
        self._update_game()

    def _update_snakes_direction(self):
        target_ppos = QtGui.QCursor().pos()
        target_pos = QPoint(*convert_to_field_pos(to_tuple(target_ppos), self.cell_size()))
        snake_pos = self._game.snake.pos()
        radius = target_pos - snake_pos
        direction_x, direction_y = map(sign, to_tuple(radius))
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
        self._game.step()
        if self._game.collision(self._game.snake.head().pos()):
            raise RuntimeError()


def sign(num):
    return -1 if num < 0 else 1 if num > 0 else 0


def convert_to_field_pos(ppos, cell_size):
    xx, yy = ppos
    cell_size_xx, cell_size_yy = cell_size
    return xx / cell_size_xx, yy / cell_size_yy


def to_tuple(point: QPoint):
    return point.x(), point.y()
