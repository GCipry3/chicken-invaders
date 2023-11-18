from .entity import Entity
from .projectile import Projectile
import random
from env.config import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY, SCREEN_WIDTH

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.velocity = random.randint(ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY)
        self.projectiles = []

    def move(self):
        self.x += self.velocity
        if self.x > SCREEN_WIDTH - ENEMY_WIDTH or self.x < 0:
            self.velocity *= -1
            self.y += 20

    def shoot(self):
        projectile = Projectile(self.x + self.width // 2, self.y + self.height, upwards=False)
        self.projectiles.append(projectile)

    def update(self):
        self.move()
        if random.randint(0, 100) < 2:
            self.shoot()
        for projectile in self.projectiles:
            projectile.update()