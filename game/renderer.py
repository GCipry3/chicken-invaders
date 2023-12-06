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

    def render(self, painter: QPainter):
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