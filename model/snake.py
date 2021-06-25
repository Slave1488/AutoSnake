from copy import copy


class Snake:
    def __init__(self, x, y, *tail_segments):
        self.head = Head(x, y)
        self.tail = []
        for segment in tail_segments:
            self.tail.append(segment)
        self._direction = DIRECTION_NONE

    def move(self):
        self.tail.append(copy(self.head))
        self.head.move(self._direction)
        self.tail.pop(0)
        print(self.tail)

    def update_direction(self, direction):
        self._direction = direction

    def pos(self):
        return self.head.pos()


class Segment:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def pos(self):
        return self.x, self.y


class Head(Segment):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, direction):
        self.x += direction.dx
        self.y += direction.dy


class Direction:
    def __init__(self, dx, dy):
        self.dx, self.dy = dx, dy


LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)
UP = Direction(0, 1)
DOWN = Direction(0, -1)
DIRECTION_NONE = Direction(0, 0)
