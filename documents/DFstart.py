import pygame
import sys

from pygame import MOUSEBUTTONDOWN


class StartButton:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("gabriola", 100)

    def draw(self):
        start_button = self.font.render(" Start ", True, (255, 255, 255), (56, 118, 29))
        self.screen.blit(start_button, (self.screen.get_width() / 2 - start_button.get_width() / 2,
                                    self.screen.get_height() / 2 - start_button.get_height() / 2))



def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    distance = math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)
    return distance

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    start_background = pygame.image.load("Level_background.png")
    game_background = pygame.image.load("Background.jpg")
    background = start_background



    clock = pygame.time.Clock()
    start = StartButton(screen)


    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # pressed_keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                background = game_background
                start_button = pygame.Rect(self.x, self.y, 75, 75)
                if start_button.collidepoint()










        start.draw()

        pygame.display.update()

main()
