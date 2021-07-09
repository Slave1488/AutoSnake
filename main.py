import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QThread
from model.game import Game
from view.gameView import GameView
from controller.gameController import GameController

app = QtWidgets.QApplication(sys.argv)


class MainApp(QtWidgets.QMainWindow):
    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Snake')
        self.show()

    def paintEvent(self, a0):
        super().paintEvent(a0)
        qp = QPainter()
        qp.begin(self)
        self._view.draw(qp)
        self._view.draw_way(qp)
        qp.end()

    def set_view(self, view: GameView):
        self._view = view

    def __init__(self):
        super().__init__()
        self.initUI()


class GameLoop(QThread):
    FPS = 4

    def __init__(self, game):
        super().__init__()
        self._game = game

    def run(self):
        self._controller = GameController(self._game)
        next_tick_time = time.time()
        while True:
            next_tick_time += 1 / GameLoop.FPS
            self._controller.tick()
            sleepTime = next_tick_time - time.time()
            if sleepTime > 0:
                time.sleep(sleepTime)


game = Game(4, 10)

window = MainApp()

view = GameView(window, game)

window.set_view(view)

_ = GameLoop(game)
_.start()

sys.exit(app.exec_())
