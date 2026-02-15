import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        radii_sum = self.radius + other.radius
        if distance < radii_sum:
            return True
        return False
        
    def update(self, dt):
        # must override
        pass
