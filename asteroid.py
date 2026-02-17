import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLIER
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        new_vel_1 = self.velocity.rotate(rand_angle)
        new_vel_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ass_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ass_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ass_1.velocity = new_vel_1 * ASTEROID_SPLIT_SPEED_MULTIPLIER
        new_ass_2.velocity = new_vel_2 * ASTEROID_SPLIT_SPEED_MULTIPLIER
        
    def update(self, dt):
        self.position += (self.velocity * dt)
