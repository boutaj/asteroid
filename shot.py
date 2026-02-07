import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x        = x
        self.y        = y
        self.radius   = radius
        self.position = pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt