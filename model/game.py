from model.snake import Segment, Snake

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake((width - 1) // 2, (height - 1) // 2, (
            Segment((width - 1) // 2, (height - 1) // 2 - 1)
        ))

    def step(self):
        self.snakes_move()

    def snakes_move(self):
        self.snake.move()

    def update_snakes_direction(self, direction):
        self.snake.update_direction(direction)
