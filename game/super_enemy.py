from .enemy import Enemy
from .projectile import Projectile
from env.config import SUPER_ENEMY_WIDTH, SUPER_ENEMY_HEIGHT, SUPER_ENEMY_VELOCITY, SUPER_ENEMY_SHOOT_PROBABILITY, SUPER_ENEMY_LIVES, PROJECTILE_THIGH_VELOCITY, PROJECTILE_THIGH_WIDTH, PROJECTILE_THIGH_HEIGHT, PROJECTILE_ENEMY_VELOCITY, PROJECTILE_ENEMY_WIDTH, PROJECTILE_ENEMY_HEIGHT


class SuperEnemy(Enemy):
    '''
    Represents a super enemy in the game.

    Attributes:
        x (int): The x-coordinate of the super enemy's position.
        y (int): The y-coordinate of the super enemy's position.
        velocity (int): The velocity at which the super enemy moves.
        projectiles (list[Projectile]): A list of projectiles shoot by the super enemy.
    '''
    def __init__(self, x, y, width=SUPER_ENEMY_WIDTH, height=SUPER_ENEMY_HEIGHT, velocity=SUPER_ENEMY_VELOCITY, lives=SUPER_ENEMY_LIVES):
        super().__init__(x=x, y=y, width=width, height=height, velocity=velocity, lives=lives)

    def shoot(self):
        '''
        Shoots projectiles with a given probability.
        '''
        return super().shoot(probability=SUPER_ENEMY_SHOOT_PROBABILITY)

    def drop_thigh(self):
        return [
            Projectile(
                x=self.x, 
                y=self.y - self.height // 2, 
                velocity=PROJECTILE_THIGH_VELOCITY, 
                width=PROJECTILE_THIGH_WIDTH, 
                height=PROJECTILE_THIGH_HEIGHT, 
                upwards=False
            ) , 
            Projectile(
                x=self.x + self.width // 2, 
                y=self.y - self.height // 2, 
                velocity=PROJECTILE_THIGH_VELOCITY, 
                width=PROJECTILE_THIGH_WIDTH, 
                height=PROJECTILE_THIGH_HEIGHT, 
                upwards=False
            ),
            Projectile(
                x=self.x + self.width, 
                y=self.y - self.height // 2, 
                velocity=PROJECTILE_THIGH_VELOCITY, 
                width=PROJECTILE_THIGH_WIDTH, 
                height=PROJECTILE_THIGH_HEIGHT, 
                upwards=False
            )
        ]
