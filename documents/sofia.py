#hi
import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode(640, 480)
    background = pygame.image.load("Background.png")
    background = pygame.transform.scale(background, (640, 480))
    screen.blit(background, (0, 0))

main()
