import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    exit = 0
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill((20, 20, 40))

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
