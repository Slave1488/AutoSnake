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
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Snake')
        self.show()

    def paintEvent(self, a0):
        super().paintEvent(a0)
        qp = QPainter()
        qp.begin(self)
        self._view.draw(qp)
        qp.end()

    def set_view(self, view):
        self._view = view


class GameLoop(QThread):
    FPS = 4

    def __init__(self, controller):
        super().__init__()
        self._controller = controller

    def run(self):
        next_tick_time = time.time()
        while True:
            next_tick_time += 1 / GameLoop.FPS
            self._controller.tick()
            sleepTime = next_tick_time - time.time()
            if sleepTime > 0:
                time.sleep(sleepTime)


game = Game(9, 7)

window = MainApp()

view = GameView(window, game)

window.set_view(view)

controller = GameController(game, window.width(), window.height())

_ = GameLoop(controller)
_.start()

sys.exit(app.exec_())
