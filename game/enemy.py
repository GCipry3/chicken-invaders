from .entity import Entity
import random
from env.config import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY, SCREEN_WIDTH

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.velocity = random.randint(ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY)

    def move(self):
        self.x += self.velocity
        if self.x > SCREEN_WIDTH - ENEMY_WIDTH or self.x < 0:
            self.velocity *= -1
            self.y += 20
