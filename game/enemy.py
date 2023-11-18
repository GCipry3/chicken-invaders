from .entity import Entity
from .projectile import Projectile
from .updatable import UpdatableInterface
import random
from env.config import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_MIN_VELOCITY, ENEMY_MAX_VELOCITY, SCREEN_WIDTH, SCREEN_HEIGHT, PROJECTILE_ENEMY_VELOCITY

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
        self.projectiles:list[Projectile] = []

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
        if random.randint(0, 100) < 1:
            projectile = Projectile(
                x=self.x + self.width // 2, 
                y=self.y + self.height, 
                velocity=PROJECTILE_ENEMY_VELOCITY,
                upwards=False
            )
            self.projectiles.append(projectile)

    def update(self):
        '''
        Updates the enemy's position and projectiles.
        '''
        self.move()
        self.shoot()
        self.update_projectiles()

    def update_projectiles(self):
        '''
        Updates the position of the enemy's projectiles.
        Removes projectiles that have reached the bottom of the screen.
        '''
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y > SCREEN_HEIGHT:
                self.projectiles.remove(projectile)