from model.game import Game
import PyQt5.QtWidgets
from PyQt5.QtGui import QPainter, QColor

WHITE = QColor(255, 255, 255)
RED = QColor(255, 0, 0)
GREEN = QColor(0, 255, 0)
PINK = QColor(255, 0, 255)
BLACK = QColor(0, 0, 0)


class GameView:
    def __init__(self, window: PyQt5.QtWidgets.QMainWindow, game: Game):
        self._window = window
        self._game = game

    def draw(self, qp: QPainter):
        qp.setBackground(BLACK)
        self._window.setStyleSheet("background-color: black;")
        w, h  = self._cell_size()
        qp.setBrush(WHITE)
        for x in range(self._game.width):
            for y in range(self._game.height):
                qp.drawRect(x * w + 1, y * h + 1, w - 2, h - 2)
        qp.setBrush(GREEN)
        pos = self._game.apple.pos()
        x, y = pos.x(), pos.y()
        qp.drawRect(x * w + 1, y * h + 1, w - 2, h - 2)
        qp.setBrush(PINK)
        for segment in self._game.snake.tail:
            pos = segment.pos()
            x, y = pos.x(), pos.y()
            qp.drawRect(x * w + 1, y * h + 1, w - 2, h - 2)
        pos = self._game.snake.pos()
        x, y = pos.x(), pos.y()
        qp.setBrush(RED)
        qp.drawRect(x * w + 1, y * h + 1, w - 2, h - 2) 

    def _cell_size(self):
        return self._width() / self._game.width,\
            self._height() / self._game.height

    def _width(self):
        return self._window.width()

    def _height(self):
        return self._window.height()
