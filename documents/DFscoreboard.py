from operator import truediv

import pygame
import sys
import random

class Fairy:
    def __init__(self,screen,x,y,filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image, (150, 150))


    def draw(self):
        self.screen.blit(self.image, (self.x,self.y))


    def move(self,movement):
        self.x = self.x + movement


        left_bound = 0 - self.image.get_width() * 0.2
        right_bound =  self.screen.get_width() - self.image.get_width() + self.image.get_width() * 0.3
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def Jump (self,Jump_hight):
        self.y = self.y + Jump_hight


    def MagicGravity(self,Gravity_amount):
        if self.y < self.screen.get_height()- self.image.get_height():
            self.y = self.y + Gravity_amount

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
        self.image.set_colorkey((255,255,0))
        self.image = pygame.transform.scale(self.image, (75, 50))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((735, 415))
    background = pygame.image.load("Background.jpg")
    screen.blit(background, (0, 0))
    testfairy = Fairy(screen,200,250,"Fairy.png")


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
            # pressed_keys = pygame.key.get_pressed()
            # if pressed_keys[pygame.K_UP]:
            #     scoreboard.score = scoreboard.score + 100
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                testfairy.Jump(-100)
            if pressed_keys[pygame.K_LEFT]:
                testfairy.move(-5)

            if pressed_keys[pygame.K_RIGHT]:
                testfairy.move(5)

            testfairy.MagicGravity(5)
            testfairy.draw()

        dust.draw(screen)
        scoreboard.draw()
        pygame.display.update()

#if __name__ == "__main__":

main()
