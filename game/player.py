from .entity import Entity
from env.config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity = PLAYER_VELOCITY

    def move_left(self):
        self.x -= self.velocity

    def move_right(self):
        self.x += self.velocity
