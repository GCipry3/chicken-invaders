import sys
from PySide6.QtWidgets import QApplication
from game.game_window import GameWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
