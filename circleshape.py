import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def colide(self, target):
        return (
            True
            if self.position.distance_to(target.position)
            <= (self.radius + target.radius)
            else False
        )

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass
