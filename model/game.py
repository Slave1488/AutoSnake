from model.apple import Apple
from model.entity import Entity
from PyQt5.QtCore import QPoint
from model.snake import DIRECTION_NONE, Segment, Snake
import random

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(
            QPoint(width // 2, height // 2),
            Segment(QPoint(width // 2, height // 2 - 1)),
        )
        self.apple = Apple(self.find_free_cell(QPoint(random.randint(0, self.width - 1), random.randint(0, self.height - 1))))

    def step(self):
        self.snakes_move()

    def respawn_apple(self):
        self.apple = Apple(self.find_free_cell(QPoint(random.randint(0, self.width - 1), random.randint(0, self.height - 1))))

    def look_at(self, cell: QPoint)-> Entity:
        cell_x, cell_y = cell.x(), cell.y()
        if cell_x < 0 or cell_y < 0 or cell_x >= self.width or cell_y >= self.height:
            return BOUND
        if hasattr(self, "apple") and cell == self.apple.pos():
            return self.apple
        if self.snake.collid(cell):
            return self.snake.head() if cell == self.snake.pos() else Segment(cell)

    def snakes_move(self):
        self.snake.move()

    def update_snakes_direction(self, direction):
        self.snake.update_direction(direction)

    def find_free_cell(self, start_point: QPoint=QPoint(0, 0))-> QPoint:
        point = start_point
        mark = []
        stack = []
        while self.look_at(point) is not None:
            mark.append(point)
            for next_point in (
                point + QPoint(1, 0),
                point + QPoint(0, 1),
                point + QPoint(-1, 0),
                point + QPoint(0, -1),
            ):
                if next_point not in mark and self.look_at(next_point) is not BOUND:
                    stack.append(next_point)
            if stack.count == 0:
                raise RuntimeError()
            point = stack.pop()
        return point


BOUND: Entity = Entity(None)
