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
    pygame.display.set_caption("Dahlia's Flight")
    background = pygame.image.load("Background.jpg")
    clock = pygame.time.Clock()
    music = pygame.mixer.Sound("StartingScreenMusic.mp3")
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    scoreboard = Scoreboard(screen)
    testfairy = Fairy(screen,25,250,"Fairy2.png", "Fairy.png")
    image1 = pygame.image.load("pixiedust.png")
    dust = pixiedust(image1, random.randint(100, 675), random.randint(100, 300))
    items = []
    items.append(dust)
    pickup_sound = pygame.mixer.Sound("pickupPD.wav")

    while True:
        screen.blit(background, (0,0))
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    testfairy.Jump(-100)
            if event.type == pygame.QUIT:
                sys.exit()

        if pressed_keys[pygame.K_LEFT]:
            testfairy.move(-5)
        if pressed_keys[pygame.K_RIGHT]:
            testfairy.move(5)

        for item in items:
            item.draw(screen)
        if testfairy.Grab(dust):
            if dust in items:
                items.remove(dust)
                pygame.mixer.Sound.play(pickup_sound)
                scoreboard.score = scoreboard.score + 100

        testfairy.MagicGravity(5)
        testfairy.draw()
        scoreboard.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()