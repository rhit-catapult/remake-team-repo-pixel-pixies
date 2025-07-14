import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 412))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))
    background = pygame.transform.scale(background, (735, 412))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()
