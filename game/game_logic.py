from .player import Player
from .enemy import Enemy
from .super_enemy import SuperEnemy
from .projectile import Projectile
from env.config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_COUNT
from .score_board import ScoreBoard
import sys

class GameLogic:
    def __init__(self):
        self.player = None
        self.enemies:list[Enemy] = []
        self.enemies_projectiles: list[Projectile] = []
        self.enemies_thighs: list[Projectile] = []
        self.score_board = ScoreBoard()

        self.start_game()

    def start_game(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - ENEMY_HEIGHT)

        gap = SCREEN_WIDTH // ENEMY_COUNT
        for i in range(ENEMY_COUNT):
            self.enemies.append(Enemy(i * gap, 100))

    def check_next_level(self):
        if not self.enemies:
            self.next_level()
            return True
        return False
    
    def check_game_over(self):
        return self.player.lives == 0

    def update(self):
        self.player.update()
        self.update_enemy()
        self.update_enemy_projectiles()
        self.update_enemy_thighs()

        self.check_player_projectile_collisions()
        self.check_enemy_projectile_collisions()
        self.check_enemy_collisions()
        self.check_player_collisions()

        is_next_level = self.check_next_level()
        is_game_over = self.check_game_over()
        
        return is_next_level, is_game_over

    def update_enemy(self):
        for enemy in self.enemies:
            if enemy.lives <= 0:
                self.enemies_thighs.extend(enemy.drop_thigh())
                
                self.score_board.chicken_kills += 1
                self.enemies.remove(enemy)
            else:
                enemy.update()
                projectile = enemy.shoot()
                if projectile:
                    self.enemies_projectiles.append(projectile)

    def next_level(self):
        self.score_board.level += 1

        # Generate the enemies
        nr_of_enemies = ENEMY_COUNT + self.score_board.level // 2
        gap = SCREEN_WIDTH // nr_of_enemies
        for i in range(nr_of_enemies):
            self.enemies.append(Enemy(i * gap, 100))

        # Generate the super enemies
        nr_of_super_enemies = self.score_board.level
        gap = SCREEN_WIDTH // nr_of_super_enemies
        for i in range(self.score_board.level):
            self.enemies.append(SuperEnemy(i * gap, 100))
        
        self.enemies_projectiles: list[Projectile] = []
        self.enemies_thighs: list[Projectile] = []
        self.player.projectiles: list[Projectile] = []

    def update_enemy_projectiles(self):
        for projectile in self.enemies_projectiles:
            projectile.update()
            if projectile.y > SCREEN_HEIGHT:
                self.enemies_projectiles.remove(projectile)

    def update_enemy_thighs(self):
        for thigh in self.enemies_thighs:
            thigh.update()
            if thigh.y > SCREEN_HEIGHT:
                self.enemies_thighs.remove(thigh)

    def check_player_projectile_collisions(self):
        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if projectile.check_collision(enemy):
                    self.player.projectiles.remove(projectile)
                    enemy.lives -= 1
                    break
        
        for projectile in self.player.projectiles:
            for enemy_projectile in self.enemies_projectiles:
                if projectile.check_collision(enemy_projectile):
                    self.player.projectiles.remove(projectile)
                    self.enemies_projectiles.remove(enemy_projectile)
                    break
    
    def check_enemy_projectile_collisions(self):
        for projectile in self.enemies_projectiles:
            if projectile.check_collision(self.player):
                self.enemies_projectiles.remove(projectile)
                self.player.lives -= 1
    
    def check_enemy_collisions(self):
        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                self.enemies.remove(enemy)
                self.player.lives -= 1
    
    def check_player_collisions(self):
        for thigh in self.enemies_thighs:
            if thigh.check_collision(self.player):
                self.enemies_thighs.remove(thigh)
                self.score_board.collected_thighs += 1
                break