from operator import truediv

import pygame
import sys

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont("gabriola", 40)

        # fonts = pygame.font.get_fonts()
        # for font in sorted(fonts):
        #     print(font)

    def draw(self):
        as_image = self.font.render(f" Score: {self.score} ", True, (255, 255, 255), (0, 0, 0))
        self.screen.blit(as_image, (5, 5))

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 412))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))
    background = pygame.transform.scale(background, (735, 412))

    scoreboard = Scoreboard(screen)
    scoreboard.draw()

    pygame.display.update()

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                scoreboard.score = scoreboard.score + 1
                print("your score went up")

main()
