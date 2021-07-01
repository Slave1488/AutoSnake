from copy import copy
from typing import List

from PyQt5.QtCore import QPoint
from model.entity import Entity


class Direction(QPoint):
    pass


class Segment(Entity):
    pass


class Snake(Entity):
    def move(self):
        if self._direction is DIRECTION_NONE:
            return
        self.tail.append(self.head())
        self._pos = self._pos + self._direction
        self.tail.pop(0)

    def update_direction(self, direction: Direction):
        self._direction = direction

    def collision(self, cell):
        return False

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
