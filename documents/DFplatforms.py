import pygame
import random
import sys

# player = pygame.transform.scale(pygame.image.load('Fairy.png'),(800,600))

class Platforms:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 200, 40))

    # def platform(self):


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Platforms Only")
    screen = pygame.display.set_mode((1280, 640))

    test = Platforms(screen, 0, 600)

    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        test.draw()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()





