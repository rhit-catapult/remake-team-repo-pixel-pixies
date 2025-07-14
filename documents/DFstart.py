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

class StartButton:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("gabriola", 100)

    def draw(self):
        as_image = self.font.render(" Start ", True, (255, 255, 255), (56, 118, 29))
        self.screen.blit(as_image, (300, 200))

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))

    scoreboard = Scoreboard(screen)
    clock = pygame.time.Clock()
    start = StartButton(screen)
    start.draw()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                scoreboard.score = scoreboard.score + 100

        scoreboard.draw()
        pygame.display.update()

main()
