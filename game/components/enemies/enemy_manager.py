import random
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update (self, game):
        
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw (self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if enemy_type ==1:
            enemy = Enemy()
        else:
            enemy = Enemy()
            enemy.rect.y = enemy.Y_POS - 70
           # print(enemy.rect.y)
            x_speed = 5
            y_speed = 1
            move_x_for = [30, 100]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for, enemy.rect.y)

        if len(self.enemies) < 4:
           self.enemies.append(enemy)
           