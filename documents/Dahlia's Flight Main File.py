import pygame
import sys

class Fairy:
    def __init__(self,screen,x,y,filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (150, 150))

    def draw(self):
        self.screen.blit(self.image, (self.x,self.y))


    def move(self,movement):
        self.x = self.x + movement
        self.y = self.y + movement

        left_bound = 0 - self.image.get_width() / 2
        right_bound = self.screen.get_width() / 2 - self.image.get_width() / 2
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def Jump (self,Jump_hight):
        self.y = self.y + Jump_hight


    #def lives(self):



def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    pygame.display.set_caption("Dahlia's Flight")
    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    testfairy = Fairy(screen,200,250,"Fairy.png")


    while True:
        clock.tick(60)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    testfairy.Jump(-20)
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            testfairy.move(-5)

        if pressed_keys[pygame.K_RIGHT]:
            testfairy.move(5)

        testfairy.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()