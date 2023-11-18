from .entity import Entity
from .projectile import Projectile
from .updatable import UpdatableInterface
from env.config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_SHOT_DELAY, SCREEN_WIDTH, PROJECTILE_PLAYER_VELOCITY
import time

class Player(Entity, UpdatableInterface):
    """
    The Player class represents the player entity in the game.
    It inherits from the Entity class and implements the UpdatableInterface.

    Attributes:
        x (int): The x-coordinate of the player's position.
        y (int): The y-coordinate of the player's position.
        velocity (int): The velocity of the player's movement.
        projectiles (list[Projectile]): The list of projectiles fired by the player.
        last_shot_time (float): The time when the player last shot a projectile.
        shot_delay (float): The delay between consecutive shots.
    """
    
    def __init__(self, x, y):
        super().__init__(x=x, y=y, width=PLAYER_WIDTH, height=PLAYER_HEIGHT)
        self.velocity = PLAYER_VELOCITY
        self.projectiles:list[Projectile] = []
        self.last_shot_time = 0
        self.shot_delay = PLAYER_SHOT_DELAY

    def move_left(self):
        """
        Moves the player to the left by subtracting the velocity from the x-coordinate.
        """
        self.x -= self.velocity

    def move_right(self):
        """
        Moves the player to the right by adding the velocity to the x-coordinate.
        """
        self.x += self.velocity

    def start_moving_left(self):
        """
        Starts the player's left movement by setting the moving_left flag to True.
        """
        self.moving_left = True

    def stop_moving_left(self):
        """
        Stops the player's left movement by setting the moving_left flag to False.
        """
        self.moving_left = False

    def start_moving_right(self):
        """
        Starts the player's right movement by setting the moving_right flag to True.
        """
        self.moving_right = True

    def stop_moving_right(self):
        """
        Stops the player's right movement by setting the moving_right flag to False.
        """
        self.moving_right = False

    def update(self):
        """
        Updates the player's state by calling the update_player and update_projectiles methods.
        """
        self.update_player()
        self.update_projectiles()

    def shoot(self):
        """
        Fires a projectile from the player if the shot delay has passed since the last shot.
        """
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shot_delay:
            projectile = Projectile(
                x=self.x + self.width // 2, 
                y=self.y, 
                velocity=PROJECTILE_PLAYER_VELOCITY, 
                upwards=True
            )
            self.projectiles.append(projectile)
            self.last_shot_time = current_time
    
    def update_player(self):
        """
        Updates the player's position based on the movement flags and ensures it stays within the screen boundaries.
        """
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()
        self.x=max(0, min(self.x, SCREEN_WIDTH - self.width))

    def update_projectiles(self):
        """
        Updates the state of the player's projectiles by calling their update method.
        Removes projectiles that have gone off the screen.
        """
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y < 0:
                self.projectiles.remove(projectile)