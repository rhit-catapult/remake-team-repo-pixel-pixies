import pygame
import sys
import random


class Fairy:
    def __init__(self,screen,x,y,Leftfile,Rightfile):
        self.screen = screen
        self.x = x
        self.y = y

        self.imageRight = pygame.image.load(Rightfile)
        self.imageRight.set_colorkey((255, 255, 255))
        self.imageRight = pygame.transform.scale(self.imageRight, (150, 150))
        self.imagedraw = self.imageRight

        self.imageLeft = pygame.image.load(Leftfile)
        self.imageLeft.set_colorkey((255, 255, 255))
        self.imageLeft = pygame.transform.scale(self.imageLeft, (150, 150))

    def draw(self):
        self.screen.blit(self.imagedraw, (self.x,self.y))

    def move(self, movement):
        self.x = self.x + movement
        self.imagedraw = self.imageRight
        if movement < 0:
            self.imagedraw = self.imageLeft

        left_bound = 0 - self.imagedraw.get_width() * 0.2
        right_bound = self.screen.get_width() - self.imagedraw.get_width() + self.imagedraw.get_width() * 0.3
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def Jump (self,Jump_hight):
        self.y = self.y + Jump_hight
        self.Hightlimit()

    def MagicGravity(self,Gravity_amount):
        if self.y < self.screen.get_height()- self.imageRight.get_height():
            self.y = self.y + Gravity_amount

    def Hightlimit(self):
        if self.y < 0:
            self.y = 0

    def Grab (self, dust):
        hero_grab = pygame.Rect(self.x, self.y, 75, 75)
        return hero_grab.collidepoint((dust.x, dust.y))

    def Land (self, platform):
        hero_land = pygame.Rect(self.x, self.y + 100, 150, 150)
        return hero_land.colliderect(platform.rect)


def main():
    pygame.init()
    IMAGE_X = 735
    IMAGE_Y = 415
    screen = pygame.display.set_mode((IMAGE_X, IMAGE_Y))
    testfairy = Fairy(screen, 25, 250, "Fairy2.png", "Fairy.png")

    while True:

        screen.blit(background, (0, 0))
        clock.tick(60)

        start_background = pygame.image.load("Level_background.png")
        game_background = pygame.image.load("Background.jpg")
        game_background = pygame.transform.scale(game_background, (IMAGE_X, IMAGE_Y))
        start_background = pygame.transform.scale(start_background, (IMAGE_X, IMAGE_Y))
        background = start_background


        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    testfairy.Jump(-100)

                testfairy.draw()

                pygame.display.update()

if __name__ == "__main__":
    main()