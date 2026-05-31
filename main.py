import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player as Player
import asteroid as Asteroid
import asteroidfield as af
import shot as Shot
import sys

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.Player.containers = (updatable, drawable)
    Asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    af.AsteroidField.containers = (updatable)
    Shot.Shot.containers = (shots, updatable, drawable)
    
    player = Player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = af.AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for group in updatable:
            group.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
               log_event("player_hit")
               print("Game over!") 
               sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        
        for group in drawable:
            group.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #print(f"{dt}")
        
if __name__ == "__main__":
    main()
