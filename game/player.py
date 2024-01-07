from .entity import Entity
from .projectile import Projectile
from .updatable import UpdatableInterface
from env.config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_SHOOT_DELAY, SCREEN_WIDTH, PROJECTILE_PLAYER_VELOCITY, PROJECTILE_PLAYER_HEIGHT, PROJECTILE_PLAYER_WIDTH
import time

class Player(Entity, UpdatableInterface):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, width=PLAYER_WIDTH, height=PLAYER_HEIGHT)
        self.velocity = PLAYER_VELOCITY
        self.projectiles:list[Projectile] = []
        self.last_shoot_time = 0
        self.shoot_delay = PLAYER_SHOOT_DELAY
        self.lives = 3

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
        self.update_player()
        self.update_projectiles()

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shoot_time >= self.shoot_delay:
            projectile = Projectile(
                x=self.x + self.width // 2, 
                y=self.y, 
                velocity=PROJECTILE_PLAYER_VELOCITY, 
                width=PROJECTILE_PLAYER_WIDTH,
                height=PROJECTILE_PLAYER_HEIGHT,
                upwards=True
            )
            self.projectiles.append(projectile)
            self.last_shoot_time = current_time
    
    def update_player(self):
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()
        self.x=max(0, min(self.x, SCREEN_WIDTH - self.width))

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y < 0:
                self.projectiles.remove(projectile)