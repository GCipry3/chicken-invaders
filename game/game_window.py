from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QKeyEvent
from .game_logic import GameLogic
from .input_handler import InputHandler
from .renderer import Renderer
from env.config import GAME_FPS, SCREEN_HEIGHT, SCREEN_WIDTH

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chicken Invaders")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        self.game_logic = GameLogic()
        self.input_handler = InputHandler(self.game_logic.player)
        self.renderer = Renderer(self.game_logic)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(1000 // GAME_FPS)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderer.render(painter)

    def update_game(self):
        self.input_handler.update()
        self.game_logic.update()
        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        self.input_handler.handle_key_event(event.key(), True)

    def keyReleaseEvent(self, event: QKeyEvent):
        self.input_handler.handle_key_event(event.key(), False)
