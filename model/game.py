from PyQt5.QtCore import QPoint
from model.snake import Segment, Snake

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(
            QPoint((width - 1) // 2, (height - 1) // 2),
            Segment(QPoint((width - 1) // 2, (height - 1) // 2 - 1)),
        )

    def step(self):
        self.snakes_move()

    def collision(self, cell: QPoint):
        cell_x, cell_y = cell.x(), cell.y()
        if cell_x < 0 or cell_y < 0 or cell_x >= self.width or cell_y >= self.height:
            return True
        return self.snake.collision(cell)

    def snakes_move(self):
        self.snake.move()

    def update_snakes_direction(self, direction):
        self.snake.update_direction(direction)
