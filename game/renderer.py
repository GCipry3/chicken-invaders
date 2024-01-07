from PySide6.QtGui import QPainter, QColor, QFont
from .game_logic import GameLogic
from env.config import SCREEN_HEIGHT, SCREEN_WIDTH

class Renderer:
    """
    The Renderer class is responsible for rendering the game objects on the screen.

    Attributes:
        game_logic (GameLogic): An instance of the GameLogic class.

    """

    def __init__(self, game_logic: GameLogic):
        self.game_logic = game_logic
    
    def render_menu(self, painter: QPainter):
        """
        Renders the menu on the screen using the provided QPainter object.
        """
        painter.setFont(QFont("Arial", 24, QFont.Bold))

        text = "Chicken Invaders"
        text_width = painter.fontMetrics().horizontalAdvance(text)  
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 - 25, text)

        text = "Press Space to start the game!"
        text_width = painter.fontMetrics().horizontalAdvance(text)  
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 + 25, text)


    def render_game(self, painter: QPainter):
        """
        Renders the game objects on the screen using the provided QPainter object.
        """
        player = self.game_logic.player

        painter.setBrush(QColor(173, 216, 230))  # Light Blue
        painter.drawRect(player.x, player.y, player.width, player.height)

        painter.setBrush(QColor("blue"))
        for projectile in self.game_logic.player.projectiles:
            painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)

        
        painter.setBrush(QColor(144, 238, 144)) # Light Green
        for enemy in self.game_logic.enemies:
            painter.drawRect(enemy.x, enemy.y, enemy.width, enemy.height)
            
        painter.setBrush(QColor("white"))
        for projectile in self.game_logic.enemies_projectiles:
            painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)

        painter.setBrush(QColor("brown"))
        for thigh in self.game_logic.enemies_thighs:
            painter.drawEllipse(thigh.x, thigh.y, thigh.width, thigh.height)
        
        painter.setBrush(QColor("black"))
        painter.setFont(QFont("Arial", 20))
        painter.drawText(10, 20, f"Lives: {self.game_logic.player.lives}")
        painter.drawText(10, 50, f"Level: {self.game_logic.score_board.level}")

    def render_game_over(self, painter: QPainter):
        """
        Renders the game over screen on the screen using the provided QPainter object.
        """
        painter.setFont(QFont("Arial", 40, QFont.Bold))

        text = "Game Over!"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 - 100, text)

        painter.setFont(QFont("Arial", 24, QFont.Bold))

        text = f"Level: {self.game_logic.score_board.level}"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 - 30, text)

        text = f"Chicken Kills: {self.game_logic.score_board.chicken_kills}"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2, text)

        text = f"Chicken Thighs: {self.game_logic.score_board.collected_thighs}"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 + 30, text)

        text = "Press Space to restart the game!"
        text_width = painter.fontMetrics().horizontalAdvance(text)
        painter.drawText((SCREEN_WIDTH - text_width) // 2, SCREEN_HEIGHT // 2 + 60, text)