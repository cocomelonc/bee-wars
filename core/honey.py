import pygame

# honey - collect by player
class Honey():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/world/honey-world.png")
        self.x, self.y = x, y
        self.screen = screen
        self.drawing = False

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

