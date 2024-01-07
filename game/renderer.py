from PySide6.QtGui import QPainter
from .game_logic import GameLogic

class Renderer:
    """
    The Renderer class is responsible for rendering the game objects on the screen.

    Attributes:
        game_logic (GameLogic): An instance of the GameLogic class.

    """

    def __init__(self, game_logic: GameLogic):
        self.game_logic = game_logic

    def render_game(self, painter: QPainter):
        """
        Renders the game objects on the screen using the provided QPainter object.
        """
        player = self.game_logic.player

        painter.drawRect(player.x, player.y, player.width, player.height)
        for projectile in self.game_logic.player.projectiles:
            painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)

        for enemy in self.game_logic.enemies:
            painter.drawRect(enemy.x, enemy.y, enemy.width, enemy.height)
            
        for projectile in self.game_logic.enemies_projectiles:
            painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)

        painter.drawText(10, 10, f"Lives: {self.game_logic.player.lives}")
        painter.drawText(10, 30, f"Level: {self.game_logic.score_board.level}")

    def render_menu(self, painter: QPainter):
        """
        Renders the menu on the screen using the provided QPainter object.
        """
        painter.drawText(10, 10, "Chicken Invaders")
        painter.drawText(10, 30, "Press Space to start the game!")
    
    def render_game_over(self, painter: QPainter):
        """
        Renders the game over screen on the screen using the provided QPainter object.
        """
        painter.drawText(10, 10, "Game Over!")
        painter.drawText(10, 30, f"Level: {self.game_logic.score_board.level}")
        painter.drawText(10, 50, f"Chicken Kills: {self.game_logic.score_board.chicken_kills}")
        painter.drawText(10, 70, "Press Space to restart the game!")