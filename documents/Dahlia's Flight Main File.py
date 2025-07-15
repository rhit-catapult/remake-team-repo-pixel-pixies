import pygame
import sys

class Fairy:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y


    def draw(self,filename,image):
        self.screen.blit(self.image1, (self.x,self.y))
        self.screen.blit(self.image2, (self.x,self.y))
        self.image1 = pygame.image.load(filename)
        self.image1.set_colorkey((255,255,255))
        self.image1 = pygame.transform.scale(self.image1, (150, 150))

        self.image2 = pygame.image.load(filename)
        self.image2.set_colorkey((255,255,255))
        self.image2 = pygame.transform.scale(self.image2, (150, 150))


    def move(self, movement):
        self.x = self.x + movement

        left_bound = 0 - self.image.get_width() * 0.2
        right_bound = self.screen.get_width() - self.image.get_width() + self.image.get_width() * 0.3
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def Jump (self,Jump_hight):
        self.y = self.y + Jump_hight


    def MagicGravity(self,Gravity_amount):
        if self.y < self.screen.get_height()- self.image.get_height():
            self.y = self.y + Gravity_amount


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
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    testfairy.Jump(-100)
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            testfairy.move(-5)
            testfairy.testfairy(screen,"Fairy2.png")

        if pressed_keys[pygame.K_RIGHT]:
            testfairy.move(5)

        testfairy.MagicGravity(5)
        testfairy.draw()


        pygame.display.update()


if __name__ == "__main__":
    main()