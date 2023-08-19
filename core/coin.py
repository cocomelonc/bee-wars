
import pygame
import random

# player's prize coin for collect
class CoinSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(CoinSprite, self).__init__()
        self.screen = screen
        self.x, self.y = x, y
        self.img = [pygame.image.load("./images/world/coin-gold_{}.png".format(i+1)) for i in range(7)]
        self.index = random.choice(range(7))
        self.image = self.img[self.index]
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def update(self):
        self.index += 1
        if self.index >= len(self.img) * 30:
            self.index = 0
        if self.index % 30 == 0:
            self.image = self.img[int(self.index/30)]
        super(CoinSprite, self).update()

class Coin(pygame.sprite.Group):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.coin_sprite = CoinSprite(self.screen, x, y)
        self.x, self.y = self.coin_sprite.x, self.coin_sprite.y
        self.centerx, self.centery = self.coin_sprite.rect.centerx, self.coin_sprite.rect.centery
        super(Coin, self).__init__(self.coin_sprite)


