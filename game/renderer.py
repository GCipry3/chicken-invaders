from PySide6.QtGui import QPainter

class Renderer:
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def render(self, painter: QPainter):
        player = self.game_logic.player
        painter.drawRect(player.x, player.y, player.width, player.height)

        for enemy in self.game_logic.enemies:
            painter.drawRect(enemy.x, enemy.y, enemy.width, enemy.height)

        for projectile in self.game_logic.player.projectiles:
            painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)

        for enemy in self.game_logic.enemies:
            for projectile in enemy.projectiles:
                painter.drawRect(projectile.x, projectile.y, projectile.width, projectile.height)