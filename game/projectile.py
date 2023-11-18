from .entity import Entity
from .updatable import UpdatableInterface
from env.config import PROJECTILE_WIDTH, PROJECTILE_HEIGHT

class Projectile(Entity, UpdatableInterface):
    """
    Represents a projectile in the game.

    Attributes:
    - x: The x-coordinate of the projectile.
    - y: The y-coordinate of the projectile.
    - velocity: The velocity of the projectile.
    - upwards: A boolean indicating whether the projectile moves upwards or downwards.
    """

    def __init__(self, x, y, velocity, upwards=True):
        super().__init__(x=x, y=y, width=PROJECTILE_WIDTH, height=PROJECTILE_HEIGHT)
        self.velocity = velocity
        self.upwards = upwards 

    def move(self):
        """
        Moves the projectile based on its velocity and direction.
        If the projectile is set to move upwards, it decreases its y-coordinate.
        If the projectile is set to move downwards, it increases its y-coordinate.
        """
        if self.upwards:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def update(self):
        """
        Updates the state of the projectile.
        Calls the move() method to move the projectile.
        """
        self.move()