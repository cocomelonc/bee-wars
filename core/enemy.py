# -*- coding: utf-8 -*-
import pygame
import random

# enemy sprite
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, face):
        super(EnemySprite, self).__init__()
        self.screen = screen
        self.left, self.right, self.up, self.down = [], [], [], []
        enemy_type = random.choice([str(i) for i in range(1, 4)])
        for i in range(3):
            self.left.append(pygame.image.load("./images/enemies/enemy{}-left_{}.png".format(enemy_type, i+1)))
            self.right.append(pygame.image.load("./images/enemies/enemy{}-right_{}.png".format(enemy_type, i+1)))
            self.down.append(pygame.image.load("./images/enemies/enemy{}-down_{}.png".format(enemy_type, i+1)))
            self.up.append(pygame.image.load("./images/enemies/enemy{}-up_{}.png".format(enemy_type, i+1)))
        self.index = 0
        self.image = self.right[self.index]
        self.x, self.y, self.face = x, y, face
        self.right_x, self.left_x = x + random.randint(64, 72), x - random.randint(64, 72)
        self.down_y, self.up_y = y + random.randint(64, 72), y - random.randint(64, 72)
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

    def move_left(self):
        self.face = 'left'
        self.index += 1
        if self.index >= len(self.left) * 30:
            self.index = 0
        if self.index % 30 == 0:
            self.image = self.left[int(self.index/30)]
        self.rect = pygame.Rect(self.x - 0.25, self.y, 64, 64)
        self.x -= random.uniform(0.06, 0.08)

    def move_right(self):
        self.face = 'right'
        self.index += 1
        if self.index >= len(self.right) * 30:
            self.index = 0
        if self.index % 30 == 0:
            self.image = self.right[int(self.index/30)]
        self.rect = pygame.Rect(self.x + 0.25, self.y, 64, 64)
        self.x += random.uniform(0.06, 0.08)

    def move_down(self):
        self.face = 'down'
        self.index += 1
        if self.index >= len(self.down) * 30:
            self.index = 0
        if self.index % 30 == 0:
            self.image = self.down[int(self.index/30)]
        self.rect = pygame.Rect(self.x, self.y + 0.25, 64, 64)
        self.y += random.uniform(0.06, 0.08)

    def move_up(self):
        self.face = 'up'
        self.index += 1
        if self.index >= len(self.up) * 30:
            self.index = 0
        if self.index % 30 == 0:
            self.image = self.up[int(self.index/30)]
        self.rect = pygame.Rect(self.x, self.y - 0.25, 64, 64)
        self.y -= random.uniform(0.06, 0.08)

    def update(self):
        if self.face == 'right':
            if self.x <= self.right_x and self.x <= 732:
                self.move_right()
            else:
                self.face = 'left'
        elif self.face == 'left':
            if self.x >= self.left_x and self.x >= 16:
                self.move_left()
            else:
                self.face = 'right'
        elif self.face == 'down':
            if self.y <= self.down_y and self.y <= 532:
                self.move_down()
            else:
                self.face = 'up'
        elif self.face == 'up':
            if self.y >= self.up_y and self.y >= 32:
                self.move_up()
            else:
                self.face = 'down'
        super(EnemySprite, self).update()

# enemy class - main enemy logic
class Enemy(pygame.sprite.Group):
    def __init__(self, screen, x, y, face):
        self.screen = screen
        self.enemy_sprite = EnemySprite(self.screen, x, y, face)
        self.x, self.y, self.face = self.enemy_sprite.x, self.enemy_sprite.y, self.enemy_sprite.face
        self.centerx, self.centery = self.enemy_sprite.rect.centerx, self.enemy_sprite.rect.centery
        self.right_x, self.left_x = self.enemy_sprite.right_x, self.enemy_sprite.left_x
        self.down_y, self.up_y = self.enemy_sprite.down_y, self.enemy_sprite.up_y
        super(Enemy, self).__init__(self.enemy_sprite)

    def update(self):
        self.x, self.y = self.enemy_sprite.x, self.enemy_sprite.y
        self.face = self.enemy_sprite.face
        self.centerx, self.centery = self.enemy_sprite.rect.centerx, self.enemy_sprite.rect.centery
        self.right_x, self.left_x = self.enemy_sprite.right_x, self.enemy_sprite.left_x
        self.down_y, self.up_y = self.enemy_sprite.down_y, self.enemy_sprite.up_y
        super(Enemy, self).update()
