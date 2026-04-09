import pygame
import random
from circleshape import *
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        roll_split = random.uniform(1, 100)
        if roll_split <= ASTEROID_SPLIT_CHANCE:
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            else:
                log_event("asteroid_split")
                angle = random.uniform(ASTEROID_SPLIT_ROTATION_MINIMUM, ASTEROID_SPLIT_ROTATION_MAXIMUM)
                split1 = self.velocity.rotate(angle)
                split2 = self.velocity.rotate(-angle)
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid1.velocity = split1 * SPLIT_ASTEROID_SPEED_MULTIPLIER
                asteroid2.velocity = split2 * SPLIT_ASTEROID_SPEED_MULTIPLIER
        else:
            return