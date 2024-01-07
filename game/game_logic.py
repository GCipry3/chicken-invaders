from .player import Player
from .enemy import Enemy
from .projectile import Projectile
from env.config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_COUNT
from random import randint
from .score_board import ScoreBoard

class GameLogic:
    """
    The GameLogic class represents the logic and mechanics of the game.
    It handles the player, enemies, and projectile collisions.

    Attributes:
        player (Player): The player object.
        enemies (list[Enemy]): The list of enemy objects.
    """

    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - ENEMY_HEIGHT)
        self.enemies:list[Enemy] = [Enemy(randint(0, SCREEN_WIDTH - ENEMY_WIDTH), 100) for _ in range(ENEMY_COUNT)]
        self.enemies_projectiles: list[Projectile] = []
        self.score_board = ScoreBoard()

    def update(self):
        """
        Updates the game logic.
        It updates the player and enemies, and checks for projectile collisions.
        """
        self.player.update()

        for enemy in self.enemies:
            enemy.update()
            if enemy.projectiles :
                self.enemies_projectiles.extend(enemy.projectiles)
                enemy.projectiles = []
        self.update_projectiles()
        self.check_projectile_collisions()

        if not self.enemies:
            self.score_board.level += 1
            self.enemies:list[Enemy] = [Enemy(randint(0, SCREEN_WIDTH - ENEMY_WIDTH), 100) for _ in range(ENEMY_COUNT + self.score_board.level)]
            self.enemies_projectiles: list[Projectile] = []


    def update_projectiles(self):
        '''
        Updates the position of the enemy's projectiles.
        Removes projectiles that have reached the bottom of the screen.
        '''
        for projectile in self.enemies_projectiles:
            projectile.update()
            if projectile.y > SCREEN_HEIGHT:
                self.enemies_projectiles.remove(projectile)

    def check_projectile_collisions(self):
        """
        Checks for projectile collisions with enemies.
        If a collision is detected, removes the projectile and enemy from the game.
        """
        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if projectile.check_collision(enemy):
                    self.player.projectiles.remove(projectile)
                    self.enemies.remove(enemy)
                    self.score_board.chicken_kills += 1
                    break
        
        for projectile in self.enemies_projectiles:
            if projectile.check_collision(self.player):
                self.enemies_projectiles.remove(projectile)
                self.player.lives -= 1
        
        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                self.enemies.remove(enemy)
                self.player.lives -= 1
        
        for projectile in self.player.projectiles:
            for enemy_projectile in self.enemies_projectiles:
                if projectile.check_collision(enemy_projectile):
                    self.player.projectiles.remove(projectile)
                    self.enemies_projectiles.remove(enemy_projectile)
                    break