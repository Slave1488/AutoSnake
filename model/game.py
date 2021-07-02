from model.apple import Apple
from model.entity import Entity
from PyQt5.QtCore import QPoint
from model.snake import Segment, Snake
import random

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(
            QPoint((width - 1) // 2, (height - 1) // 2),
            Segment(QPoint((width - 1) // 2, (height - 1) // 2 - 1)),
        )
        self.apple = Apple(QPoint(random.randint(0, self.width - 1), random.randint(0, self.height - 1)))

    def step(self):
        self.snakes_move()

    def respawn_apple(self):
        self.apple = Apple(QPoint(random.randint(0, self.width - 1), random.randint(0, self.height - 1)))

    def look_at(self, cell: QPoint)-> Entity:
        cell_x, cell_y = cell.x(), cell.y()
        if cell_x < 0 or cell_y < 0 or cell_x >= self.width or cell_y >= self.height:
            return BOUND
        if cell == self.apple.pos():
            return self.apple
        if self.snake.collid(cell):
            return self.snake.head() if cell == self.snake.pos() else Segment(cell)
        

    def snakes_move(self):
        self.snake.move()

    def update_snakes_direction(self, direction):
        self.snake.update_direction(direction)


BOUND: Entity = Entity(None)
