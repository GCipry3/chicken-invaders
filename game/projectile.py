from .entity import Entity
from .updatable import UpdatableInterface

class Projectile(Entity, UpdatableInterface):
    def __init__(self, x, y, velocity, width, height, upwards=True):
        super().__init__(x=x, y=y, width=width, height=height)
        self.velocity = velocity
        self.upwards = upwards 

    def move(self):
        if self.upwards:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def update(self):
        self.move()