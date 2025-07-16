import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Clearing.png")
    IMAGE_HEIGHT = 415
    IMAGE_WIDTH = 735
    background = pygame.transform.scale(background, (IMAGE_WIDTH, IMAGE_HEIGHT))
    image = pygame.image.load("portal.png")
    image = pygame.transform.scale(image, (300, 300))

    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Getting coordinates for platforms
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print(click_position)

        screen.blit(image, (525, 20))
        pygame.display.update()

main()
