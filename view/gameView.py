import pygame

WHITE = 255, 255, 255
RED = 255, 0, 0
PINK = 255, 0, 255
BLACK = 0, 0, 0

class GameView:
    def __init__(self, screen, game):
        self._screen = screen
        self._game = game

    def draw(self):
        self._screen.fill(BLACK)
        w, h  = self._cell_size()
        for x in range(self._game.width):
            for y in range(self._game.height):
                pygame.draw.rect(self._screen, WHITE, (x * w + 1, y * h + 1, w - 2, h - 2))
        for segment in self._game.snake.tail:
            x, y = segment.pos()
            pygame.draw.rect(self._screen, PINK, (x * w + 1, y * h + 1, w - 2, h - 2))
        x, y = self._game.snake.head.pos()
        pygame.draw.rect(self._screen, RED, (x * w + 1, y * h + 1, w - 2, h - 2))
        pygame.display.flip()

    def _cell_size(self):
        return self._width() / self._game.width,\
            self._height() / self._game.height

    def _width(self):
        return self._screen.get_width()

    def _height(self):
        return self._screen.get_height()
