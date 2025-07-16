import pygame
import sys

class Portal:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y

        #self.image = pygame.image.load("portal.png")
        # self.image.set_colorkey((255, 255, 255))
        # self.image = pygame.transform.scale(self.image, (150, 150))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Portal_Place_Pixelated.png")
    portal = Portal(screen, 100, 100, "portal.png")
    IMAGE_HEIGHT = 415
    IMAGE_WIDTH = 735
    background = pygame.transform.scale(background, (IMAGE_WIDTH, IMAGE_HEIGHT))

    portal = pygame.image.load("Portal_Place_Pixelated.png")

    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        portal.draw()
        pygame.display.update()

main()
