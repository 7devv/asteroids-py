import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
    
        pygame.Surface.fill(screen, (0, 0, 0))
        
        player.draw(screen)
        player.update(dt)
        
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000

 
    
print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")    
print(f"Screen height: {SCREEN_HEIGHT}")

    
if __name__ == "__main__":
    main()