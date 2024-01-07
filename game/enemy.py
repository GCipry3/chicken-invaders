from .entity import Entity
from .projectile import Projectile
from .updatable import UpdatableInterface
import random
from env.config import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY, SCREEN_WIDTH, SCREEN_HEIGHT, PROJECTILE_ENEMY_VELOCITY, PROJECTILE_ENEMY_HEIGHT, PROJECTILE_ENEMY_WIDTH,ENEMY_SHOT_PROBABILITY

class Enemy(Entity, UpdatableInterface):
    '''
    Represents an enemy in the game.

    Attributes:
        x (int): The x-coordinate of the enemy's position.
        y (int): The y-coordinate of the enemy's position.
        velocity (int): The velocity at which the enemy moves.
        projectiles (list[Projectile]): A list of projectiles shot by the enemy.
    '''
    def __init__(self, x, y):
        super().__init__(x=x, y=y, width=ENEMY_WIDTH, height=ENEMY_HEIGHT)
        self.velocity = random.randint(ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY)

    def move(self):
        '''
        Moves the enemy horizontally and vertically.
        If the enemy reaches the screen boundaries, it changes direction and moves down.
        '''
        self.x += self.velocity
        if self.x > SCREEN_WIDTH - ENEMY_WIDTH or self.x < 0:
            self.velocity *= -1
            #self.y += 20

    def shoot(self):
        '''
        Shoots projectiles randomly.
        There is a 2% chance of shooting a projectile on each update.
        '''
        if random.randint(0, 1000) < ENEMY_SHOT_PROBABILITY:
            return Projectile(
                x=self.x + self.width // 2, 
                y=self.y + self.height, 
                velocity=PROJECTILE_ENEMY_VELOCITY,
                width=PROJECTILE_ENEMY_WIDTH,
                height=PROJECTILE_ENEMY_HEIGHT,
                upwards=False
            )
        return None

    def update(self):
        '''
        Updates the enemy's position and projectiles.
        '''
        self.move()