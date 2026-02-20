import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          +
          f"Screen height: {SCREEN_HEIGHT}"
          )
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return       
        screen.fill("black")
        updatable.update(dt)
        for image in drawable:  
            image.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = (Clock.tick(60) * 0.001)


if __name__ == "__main__":
    main()
