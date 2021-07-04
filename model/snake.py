from functools import reduce
from model.apple import Apple
from typing import List

from PyQt5.QtCore import QPoint
from model.entity import Entity


class Direction(QPoint):
    pass


class Segment(Entity):
    pass


class Snake(Entity):
    def move(self):
        self.tail.append(self.head())
        self._pos = self.focus()
        self.tail.pop(0)

    def eat(self, apple: Apple):
        self.tail.append(Segment(apple.pos()))

    def update_direction(self, direction: Direction):
        self._direction = direction

    def focus(self):
        return self.pos() + self._direction

    def collid(self, cell: QPoint):
        return reduce(lambda acc, next: acc or next, map(lambda s: cell == s.pos(), (self.head(), *self.tail)))

    def head(self)-> Segment:
        return Segment(self._pos)

    def __init__(self, pos: QPoint, *tail_segments: Segment):
        super().__init__(pos)
        self.tail: List[Segment] = []
        for segment in tail_segments:
            self.tail.append(segment)
        self._direction = DIRECTION_NONE


class Segment(Entity):
    def __init__(self, pos: QPoint):
        super().__init__(pos)


LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)
UP = Direction(0, 1)
DOWN = Direction(0, -1)
DIRECTION_NONE = Direction(0, 0)
