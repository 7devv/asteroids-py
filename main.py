import pygame
import sys
from bullets import Shot
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 # Delta time
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
    
        screen.fill("black")
        
        for updateables in updateable:
            updateables.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill() 
                    asteroid.kill()
            
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