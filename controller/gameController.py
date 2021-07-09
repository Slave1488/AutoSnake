from typing import List
from itertools import chain

import numpy
from model.apple import Apple
from model.game import BOUND, Game
from model.snake import LEFT, RIGHT, Segment, UP, DOWN, DIRECTION_NONE
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint

skip_frame = 15


class GameController:
    def __init__(self, game: Game):
        self._game = game
        self._N = self._game.width * self._game.height
        self._way = self.build_way(self._game.snake.pos())
        self._counter_way = 0

    def tick(self):
        self._update_snakes_direction()
        self._update_game()

    def _update_snakes_direction(self):
        self._counter_way = (self._counter_way + 1) % self._N
        target_pos = self._way[self._counter_way]
        snake_pos = self._game.snake.pos()
        radius = target_pos - snake_pos
        direction_x, direction_y = map(sign, to_tuple(radius))
        if direction_x == 1:
            direction = RIGHT
        elif direction_x == -1:
            direction = LEFT
        elif direction_y == 1:
            direction = UP
        elif direction_y == -1:
            direction = DOWN
        else:
            direction = DIRECTION_NONE
        self._game.update_snakes_direction(direction)

    def _update_game(self):
        if self._game.snake._direction is DIRECTION_NONE:
            return
        let = self._game.look_at(self._game.snake.focus())
        if let is BOUND or isinstance(let, Segment):
            raise RuntimeError()
        self._game.step()
        if isinstance(let, Apple):
            self._game.snake.eat(let)
            self._game.respawn_apple()

    def build_way(self, start: QPoint)-> tuple[QPoint]:
        def neighbors(id):
            x, y = id % self._game.width, id // self._game.width
            if x != 0:
                yield id - 1
            if y != 0:
                yield id - self._game.width
            if x != self._game.width - 1:
                yield id + 1
            if y != self._game.height - 1:
                yield id + self._game.width
        def is_nearby(id_one, id_other):
            return abs(id_one % self._game.width - id_other % self._game.width) +\
                abs(id_one // self._game.width - id_other // self._game.width) <= 1
        def is_bind(*ids):
            if len(ids) < 2:
                return True
            id1, id2, *_ = ids
            stack = [id1]
            l_mark = {}
            while stack[-1] != id2:
                cur_id = stack.pop()
                l_mark[cur_id] = True
                for next_id in filter(lambda id: not mark[id] and not l_mark.get(id), neighbors(cur_id)):
                    stack.append(next_id)
                if len(stack) == 0:
                    return False
            if len(_) != 0:
                return is_bind(id1, *_)
            return True

        stack = [start.y() * self._game.width + start.x()]
        self._game.way = [stack[-1]]
        # print(f'{way[-1]}')
        mark = [False for _ in range(self._N)]
        dead_counter = 0
        miss_counter = 0
        while not (len(self._game.way) == self._N and is_nearby(self._game.way[-1], self._game.way[0])):
            mark[self._game.way[-1]] = True
            next_ids = (*filter(lambda id: not mark[id], rearrange((*neighbors(self._game.way[-1]),))),)
            if len(next_ids) != 0 and is_bind(*next_ids):
                for id in next_ids:
                    stack.append(id)
            else:
                if len(self._game.way) == self._N:
                    miss_counter += 1
                    print('-'.join(map(str, self._game.way)))
                dead_counter += 1
                was_len = len(self._game.way)
                while stack[-1] == self._game.way[-1]:
                    mark[self._game.way.pop()] = False
                    stack.pop()
                print(f'{miss_counter}\t{dead_counter}\t{was_len} - {was_len - len(self._game.way)}\t -> {len(self._game.way)} ({100 - len(self._game.way)})')
            self._game.way.append(stack[-1])
            # print(f'{" " * (len(way) - 1)}{way[-1]}')
        print('-'.join(map(str, self._game.way)))
        return *map(lambda id: QPoint(id % self._game.width, id // self._game.width), self._game.way),


def sign(num):
    return -1 if num < 0 else 1 if num > 0 else 0


def convert_to_field_pos(ppos, cell_size):
    xx, yy = ppos
    cell_size_xx, cell_size_yy = cell_size
    return xx / cell_size_xx, yy / cell_size_yy


def to_tuple(point: QPoint):
    return point.x(), point.y()


def rearrange(array):
    perm = numpy.random.permutation(len(array))
    for i in perm:
        yield array[i]