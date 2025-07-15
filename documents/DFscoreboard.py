from operator import truediv

import pygame
import sys
import random

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

class pixiedust:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.image = pygame.transform.scale(self.image, (75, 50))

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))

    scoreboard = Scoreboard(screen)
    clock = pygame.time.Clock()

    pygame.display.set_caption("Dahlia's Flight")
    image1 = pygame.image.load("pixiedust.png")
    dust = pixiedust(image1, random.randint(25, 700), 300)
    # pickup_sound = pygame.mixer.Sound("pickupPD.wav")
    WHITE = pygame.Color("white")
    BLACK = pygame.Color("black")


    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                scoreboard.score = scoreboard.score + 100

        dust.draw(screen)
        scoreboard.draw()
        pygame.display.update()

main()
