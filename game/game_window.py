from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QKeyEvent
from .game_logic import GameLogic
from .input_handler import InputHandler
from .renderer import Renderer
from env.config import GAME_FPS, SCREEN_HEIGHT, SCREEN_WIDTH

class GameWindow(QMainWindow):
    """
    The main window of the Chicken Invaders game.

    This class represents the main window of the game. It inherits from QMainWindow and provides the necessary
    functionality to handle user input, update the game logic, and render the game on the screen.

    Attributes:
        game_logic (GameLogic): The instance of the GameLogic class responsible for managing the game logic.
        input_handler (InputHandler): The instance of the InputHandler class responsible for handling user input.
        renderer (Renderer): The instance of the Renderer class responsible for rendering the game on the screen.
        timer (QTimer): The QTimer instance used to update the game at a fixed frame rate.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chicken Invaders")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        self.game_logic = GameLogic()
        self.input_handler = InputHandler(player=self.game_logic.player)
        self.renderer = Renderer(self.game_logic)
        self.game_state = 0 # 0: menu, 1: game, 2: game over

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(1000 // GAME_FPS)

    def paintEvent(self, event):
        """
        Overrides the paintEvent method of QMainWindow to render the game on the screen.
        """
        painter = QPainter(self)

        if self.game_state == 0:
            self.renderer.render_menu(painter)
        elif self.game_state == 1:
            self.renderer.render_game(painter)
        elif self.game_state == 2:
            self.renderer.render_game_over(painter)

    def reset_game(self):
        """
        Resets the game by resetting the game logic, input handler, and game state.
        """
        self.game_logic = GameLogic()
        self.input_handler = InputHandler(player=self.game_logic.player)
        self.renderer = Renderer(self.game_logic)

    def update_game(self):
        """
        Updates the game logic, input handling, and triggers a repaint of the window.
        """
        self.input_handler.update()

        if self.game_state == 0:
            if self.input_handler.key_states[Qt.Key_Space]:
                self.input_handler.key_states[Qt.Key_Space] = False
                self.game_state = 1
        elif self.game_state == 1:
            if not self.game_logic.update():
                self.game_state = 2
        elif self.game_state == 2:
            if self.input_handler.key_states[Qt.Key_Space]:
                self.reset_game()
                self.game_state = 1
        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        """
        Overrides the keyPressEvent method of QMainWindow to handle key press events.
        """
        self.input_handler.handle_key_event(event.key(), True)

    def keyReleaseEvent(self, event: QKeyEvent):
        """
        Overrides the keyReleaseEvent method of QMainWindow to handle key release events.
        """
        self.input_handler.handle_key_event(event.key(), False)
