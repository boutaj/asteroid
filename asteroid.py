import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        randomAngle = random.uniform(20, 50)

        v1 = self.velocity.rotate(randomAngle)
        v2 = self.velocity.rotate(-randomAngle)

        r1 = r2 = self.radius - ASTEROID_MIN_RADIUS

        as1 = Asteroid(self.x, self.y, r1)
        as2 = Asteroid(self.x, self.y, r2)

        as1.velocity = v1 * 1.2
        as2.velocity = v2 * 1.2



