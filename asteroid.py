import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        randomAngle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(randomAngle)
        vector2 = self.velocity.rotate(-randomAngle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        childAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        childAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)

        childAsteroid1.velocity = vector1 * 1.2
        childAsteroid2.velocity = vector2 * 1.2
