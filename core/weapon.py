import pygame

# player's weapon
class Weapon():
    def __init__(self, screen, player, direction):
        self.player = player
        self.direction = direction
        self.image = pygame.image.load("./images/world/honey-weapon.png")
        self.x, self.y = self.player.x - 4, self.player.y + 8
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.centerx, self.centery = self.rect.center
        self.screen = screen
        self.drawing, self.last_direction = False, self.player.face

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.centerx, self.centery = self.rect.center
        if self.drawing:
            if self.direction == 'left':
                if self.x >= 2:
                    self.x -= 4
            elif self.direction == 'right':
                if self.x <= 796:
                    self.x += 4
            elif self.direction == 'up':
                if self.y >= 2:
                    self.y -= 4
            elif self.direction == 'down':
                if self.y <= 796:
                    self.y += 4
            if self.x <= 4 or self.x >= 796 or self.y <= 4 or self.y >= 596:
                self.drawing = False
        else:
            if self.direction == 'left':
                self.x, self.y = self.player.x + 12, self.player.y + 24
            elif self.direction == 'right':
                self.x, self.y = self.player.x + 12, self.player.y + 24
            elif self.direction == 'up':
                self.x, self.y = self.player.x + 24, self.player.y + 16
            elif self.direction == 'down':
                self.x, self.y = self.player.x + 24, self.player.y + 16
