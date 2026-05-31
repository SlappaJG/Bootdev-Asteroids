import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
import shot

class Player(circleshape.CircleShape):
    
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_time = 0
    
    # creates triangle shape for player body
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        
    def rotate(self, dt: float) -> None:
        self.rotation += (dt*PLAYER_TURN_SPEED)

    def update(self, dt: float) -> None:
        self.shot_cooldown_time -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_time > 0:
                pass
            else:
                self.shot_cooldown_time = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
    
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        
        rotated_vector = unit_vector.rotate(self.rotation)
        
        rotated_with_vector_speed = rotated_vector * PLAYER_SPEED * dt
        
        self.position += rotated_with_vector_speed
        
    def shoot(self) -> None:
        
        if self.shot_cooldown_time > 0:
                pass
        else:
            self.shot_cooldown_time = PLAYER_SHOOT_COOLDOWN_SECONDS
                
        new_shot = shot.Shot(self.position.x, self.position.y, SHOT_RADIUS)
        
        new_shot_vector = pygame.Vector2(0, 1)
        
        new_shot.velocity = new_shot_vector
        
        rotated_new_shot = new_shot_vector.rotate(self.rotation)
        
        rotated_new_shot_with_speed = rotated_new_shot * PLAYER_SHOOT_SPEED
        
        new_shot.velocity = rotated_new_shot_with_speed