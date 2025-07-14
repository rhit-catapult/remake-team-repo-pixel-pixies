import pygame
import sys

class Fairy:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        self.image = pygame.image.load("")
        #self.image.set_colorkey((0,0,0))

    def move(self,movement):
        self.x = self.x + movement
        self.y = self.y + movement

        left_bound = 0 - self.image.get_width() / 2
        right_bound = self.screen.get_width() / 2 - self.image.get_width() / 2
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound
        # jump


    #def lives(self):



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dahlia's Flight")
    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    BLACK = (0,0,0)


    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    Fairy.Jump
            if event.type == pygame.QUIT:
                sys.exit()
                screen.fill((WHITE))

        if pressed_keys[pygame.K_LEFT]:
            Fairy.move(-5)
            Fairy.move(5)

        pygame.display.update()


main()