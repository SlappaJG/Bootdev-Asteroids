import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player as p

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()  
    p.Player.containers = (updatable, drawable)
    player = p.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
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
        
        for group in drawable:
            player.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #print(f"{dt}")
        
if __name__ == "__main__":
    main()
