from PyQt5.QtCore import QPoint

class Entity:
    def pos(self) -> QPoint:
        return self._pos

    def __eq__(self, o: object) -> bool:
        if type(o) is not type(self):
            return False
        o_entity: Entity = o
        return self._pos == o_entity._pos

    def __init__(self, pos: QPoint) -> None:
        self._pos = pos
        