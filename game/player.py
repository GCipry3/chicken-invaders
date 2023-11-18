from .entity import Entity
from .projectile import Projectile
from env.config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_SHOT_DELAY
import time

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity = PLAYER_VELOCITY
        self.projectiles = []
        self.last_shot_time = 0
        self.shot_delay = PLAYER_SHOT_DELAY

    def move_left(self):
        self.x -= self.velocity

    def move_right(self):
        self.x += self.velocity

    def start_moving_left(self):
        self.moving_left = True

    def stop_moving_left(self):
        self.moving_left = False

    def start_moving_right(self):
        self.moving_right = True

    def stop_moving_right(self):
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shot_delay:
            projectile = Projectile(self.x + self.width // 2, self.y, upwards=True)
            self.projectiles.append(projectile)
            self.last_shot_time = current_time
