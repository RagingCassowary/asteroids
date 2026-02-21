import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return       
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for image in drawable:  
            image.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = (Clock.tick(60) * 0.001)


if __name__ == "__main__":
    main()
