from .player import Player
from .enemy import Enemy
from env.config import SCREEN_WIDTH, SCREEN_HEIGHT

class GameLogic:
    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.enemies = [Enemy(100, 100), Enemy(200, 100), Enemy(300, 100)]

    def update(self):
        self.player.update()
        self.player.x = max(0, min(self.player.x, SCREEN_WIDTH - self.player.width))

        for enemy in self.enemies:
            enemy.update()
            self.handle_projectiles(enemy.projectiles, is_enemy=True)

        self.handle_projectiles(self.player.projectiles, is_enemy=False)

        self.check_projectile_collisions()

    def handle_projectiles(self, projectiles, is_enemy):
        for projectile in projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > SCREEN_HEIGHT:
                projectiles.remove(projectile)

    def check_projectile_collisions(self):
        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if projectile.check_collision(enemy):
                    self.player.projectiles.remove(projectile)
                    self.enemies.remove(enemy)
                    break
