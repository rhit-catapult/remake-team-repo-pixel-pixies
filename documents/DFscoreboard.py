import pygame
import sys

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont("gabriola", 50)

        fonts = pygame.font.get_fonts()
        for font in sorted(fonts):
            print(font)

    def draw(self):
        as_image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(as_image, (175, 5))

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 412))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))
    background = pygame.transform.scale(background, (735, 412))

    scoreboard = Scoreboard(screen)
    scoreboard.draw()

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
