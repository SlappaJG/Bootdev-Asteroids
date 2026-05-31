import circleshape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(circleshape.CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y,radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float):
        self.position += (self.velocity * dt)