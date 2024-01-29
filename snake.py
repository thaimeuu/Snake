import pygame


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.speed = 5
        self.width = 20
        self.length = 20
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def update(self, surface):
        if self.right:
            self.x += self.speed
        elif self.left:
            self.x -= self.speed
        elif self.up:
            self.y -= self.speed
        elif self.down:
            self.y += self.speed

        if not self.alive:
            self.right, self.left, self.up, self.down = False, False, False, False

        pygame.draw.rect(surface, "green", (self.x, self.y, self.width, self.length))
