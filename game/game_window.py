from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
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
        self.input_handler = InputHandler(player=self.game_logic.player)
        self.renderer = Renderer(self.game_logic)
        self.game_state = 0 # 0: menu, 1: game, 2: next level, 3: game over

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(1000 // GAME_FPS)

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.game_state == 0:
            self.renderer.render_menu(painter)
        elif self.game_state == 1:
            self.renderer.render_game(painter)
        elif self.game_state == 2:
            self.renderer.render_next_level_screen(painter)
        elif self.game_state == 3:
            self.renderer.render_game_over(painter)

    def reset_game(self):
        """
        Resets the game by resetting the game logic, input handler, and game state.
        """
        self.game_logic = GameLogic()
        self.input_handler = InputHandler(player=self.game_logic.player)
        self.renderer = Renderer(self.game_logic)

    def update_game(self):
        self.input_handler.update()

        if self.game_state == 0:
            if self.input_handler.key_states[Qt.Key_Up]:
                self.input_handler.key_states[Qt.Key_Up] = False
                self.game_state = 1
        elif self.game_state == 1:
            is_next_level, is_game_over = self.game_logic.update()
            if is_next_level:
                self.game_state = 2
            if is_game_over:
                self.game_state = 3
        elif self.game_state == 2:
            if self.input_handler.key_states[Qt.Key_Up]:
                self.game_state = 1
        elif self.game_state == 3:
            if self.input_handler.key_states[Qt.Key_Up]:
                self.reset_game()
                self.game_state = 1
        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        self.input_handler.handle_key_event(event.key(), True)

    def keyReleaseEvent(self, event: QKeyEvent):
        self.input_handler.handle_key_event(event.key(), False)
