import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
    
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for updateables in updateable:
            updateables.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
                
        
        for drawables in drawable:
            drawables.draw(screen)
        

        
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000

 
    
print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")    
print(f"Screen height: {SCREEN_HEIGHT}")

    
if __name__ == "__main__":
    main()