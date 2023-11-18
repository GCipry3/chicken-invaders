from .entity import Entity
from env.config import PROJECTILE_VELOCITY, PROJECTILE_WIDTH, PROJECTILE_HEIGHT

class Projectile(Entity):
    def __init__(self, x, y, upwards=True):
        super().__init__(x, y, PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
        self.velocity = PROJECTILE_VELOCITY
        self.upwards = upwards 

    def move(self):
        if self.upwards:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def update(self):
        self.move()