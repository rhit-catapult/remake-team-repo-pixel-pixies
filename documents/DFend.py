import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Portal_Place_Pixelated.png")
    IMAGE_HEIGHT = 415
    IMAGE_WIDTH = 735
    background = pygame.transform.scale(background, (IMAGE_WIDTH, IMAGE_HEIGHT))
    image = pygame.image.load("portal.png")
    image = pygame.transform.scale(image, (225, 225))

    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(image, (290, 100))
        pygame.display.update()

main()
