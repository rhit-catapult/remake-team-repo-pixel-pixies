import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Portal_Place.jpg")
    screen.blit(background, (0, 0))

    # scoreboard = Scoreboard(screen)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main()
