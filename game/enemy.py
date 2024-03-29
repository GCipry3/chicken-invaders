from .entity import Entity
from .projectile import Projectile
from .updatable import UpdatableInterface
import random
from env.config import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_VELOCITY, SCREEN_WIDTH, SCREEN_HEIGHT, PROJECTILE_ENEMY_VELOCITY, PROJECTILE_ENEMY_HEIGHT, PROJECTILE_ENEMY_WIDTH,ENEMY_SHOOT_PROBABILITY, PROJECTILE_THIGH_VELOCITY, PROJECTILE_THIGH_WIDTH, PROJECTILE_THIGH_HEIGHT

class Enemy(Entity, UpdatableInterface):
    def __init__(self, x, y, width=ENEMY_WIDTH, height=ENEMY_HEIGHT, velocity=ENEMY_VELOCITY, lives=1):
        super().__init__(x=x, y=y, width=width, height=height)
        self.velocity = velocity
        self.lives = lives

    def move(self):
        self.x += self.velocity
        if self.x > SCREEN_WIDTH - self.width or self.x < 0:
            self.velocity *= -1
            #self.y += 20

    def shoot(self ,probability=ENEMY_SHOOT_PROBABILITY):
        if random.randint(0, 1000) < probability:
            return Projectile(
                x=self.x + self.width // 2, 
                y=self.y + self.height, 
                velocity=PROJECTILE_ENEMY_VELOCITY,
                width=PROJECTILE_ENEMY_WIDTH,
                height=PROJECTILE_ENEMY_HEIGHT,
                upwards=False
            )
        return None

    def drop_thigh(self):
        return [ Projectile(
            x=self.x, 
            y=self.y, 
            velocity=PROJECTILE_THIGH_VELOCITY, 
            width=PROJECTILE_THIGH_WIDTH, 
            height=PROJECTILE_THIGH_HEIGHT, 
            upwards=False
        ) ]

    def update(self):
        self.move()