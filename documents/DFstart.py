import pygame
import sys

from pygame import MOUSEBUTTONDOWN


class StartButton:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("gabriola", 100)
        self.start_button = self.font.render(" Start ", True, (255, 255, 255), (56, 118, 29))
        self.x = self.screen.get_width() / 2 - self.start_button.get_width() / 2
        self.y = self.screen.get_height() / 2 - self.start_button.get_height() / 2
        self.rect = pygame.Rect(self.x, self.y, self.start_button.get_width(), self.start_button.get_height())


    def draw(self):
        self.screen.blit(self.start_button, (self.x, self.y))

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
                # print("clicked")
                retangal =  start.rect
                # print(retangal.x, retangal.y)
                result = retangal.collidepoint(event.pos)
                # print(result)
                if retangal.collidepoint(event.pos):
                    background = game_background
                    # print("I clicked!!")

        if background == game_background:
            pass
        else:
            start.draw()


        pygame.display.update()

if __name__ == "__main__":
    main()
