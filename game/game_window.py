from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QKeyEvent
from .player import Player
from .enemy import Enemy
from env.config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FPS

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chicken Invaders")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.enemies = [Enemy(100, 100), Enemy(200, 100), Enemy(300, 100)]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(1000 // GAME_FPS)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.player.x, self.player.y, self.player.width, self.player.height)
        for enemy in self.enemies:
            painter.drawRect(enemy.x, enemy.y, enemy.width, enemy.height)

    def update_game(self):
        for enemy in self.enemies:
            enemy.move()
        self.update() 

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Left:
            self.player.move_left()
        elif event.key() == Qt.Key_Right:
            self.player.move_right()
        self.update()
