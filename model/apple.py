from PyQt5.QtCore import QPoint
from model.entity import Entity


class Apple(Entity):
    def __init__(self, pos: QPoint):
        super().__init__(pos)
