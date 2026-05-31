import circleshape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, NEW_ASTEROID_SPEED_BOOST
from logger import log_event
import random

class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y,radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angel = random.uniform(20, 50)

            new_asteroid_velocity = self.velocity.rotate(new_angel)
            new_asteroid2_velocity = self.velocity.rotate(-new_angel)
            
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            
            asteroid1.velocity = new_asteroid_velocity * NEW_ASTEROID_SPEED_BOOST
            asteroid2.velocity = new_asteroid2_velocity * NEW_ASTEROID_SPEED_BOOST
            