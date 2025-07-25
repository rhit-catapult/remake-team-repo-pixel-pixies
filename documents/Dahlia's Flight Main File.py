import pygame
import sys
import random
import DFstart


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

    def bound(self):
        if self.x > 600:
            self.x = 600

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
        hero_land = pygame.Rect(self.x + 25, self.y + 40, 75, 75)
        return hero_land.colliderect(platform.rect)


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


class Platforms:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 100, 40)

    def draw(self):
        pygame.draw.rect(self.screen, (112, 59, 40), (self.x, self.y, 100, 40))

def main():
    pygame.init()
    IMAGE_X = 735
    IMAGE_Y = 415
    font = pygame.font.Font(None, 25)
    screen = pygame.display.set_mode((IMAGE_X, IMAGE_Y))
    #screen = pygame.display.set_mode((735, 415))
    pygame.display.set_caption("Dahlia's Flight")

    start_background = pygame.image.load("Level_background.png")
    game_background = pygame.image.load("Background.jpg")
    end_background = pygame.image.load("Clearing.png")
    end_background = pygame.transform.scale(end_background, (735, 415))
    game_background = pygame.transform.scale(game_background, (IMAGE_X, IMAGE_Y))
    start_background = pygame.transform.scale(start_background, (IMAGE_X, IMAGE_Y))
    background = start_background
    portal = pygame.image.load("portal.png")
    portal = pygame.transform.scale(portal, (300, 300))

    clock = pygame.time.Clock()
    start = DFstart.StartButton(screen)
    instruction_text = "Dahlia's Flight"
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    music = pygame.mixer.Sound("StartingScreenMusic.mp3")
    WHITE = (255,255,255)
    BLACK = (0,0,0)

    scoreboard = Scoreboard(screen)
    testfairy = Fairy(screen,25,250,"Fairy2.png", "Fairy.png")
    image1 = pygame.image.load("pixiedust.png")
    dust = pixiedust(image1, random.randint(200, 600), random.randint(50, 300))
    items = []
    items.append(dust)
    pickup_sound = pygame.mixer.Sound("pickupPD.wav")

    my_platform = []
    platform_positions = [(600, 190),
                          (150, 300),
                           (345, 160)]

    for x,y in platform_positions:
        new_platforms = Platforms(screen, x, y)
        my_platform.append(new_platforms)

    while True:
        screen.blit(background, (0,0))
        clock.tick(60)

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                retangal = start.rect
                if retangal.collidepoint(event.pos):
                    background = game_background

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    testfairy.Jump(-100)

            if testfairy.x == 600 and scoreboard.score > 400:
                background = end_background

        if background == end_background:
            screen.blit(portal, (screen.get_width()/2-120, screen.get_height()/2-100))
            testfairy.draw()
            scoreboard.draw()
            testfairy.MagicGravity(5)
            font2 = pygame.font.SysFont("Times New Roman", 45)
            font3 = pygame.font.SysFont("Times New Roman", 15)
            caption2 = font2.render("Congrats! You won!!", True, WHITE)
            screen.blit(caption2, (screen.get_width()/2 - caption2.get_width()/2, screen.get_height()/2-150))
            caption3 = font3.render("(Also sorry our portal doesn't work)", True, WHITE)
            screen.blit(caption3, (screen.get_width()/2 - caption2.get_width()/2 + 85, screen.get_height()/2+165))
            if pressed_keys[pygame.K_LEFT]:
                testfairy.move(-5)
            if pressed_keys[pygame.K_RIGHT]:
                testfairy.move(5)

        if background == game_background:
            hit_a_platform = False
            for platform in my_platform:
                platform.draw()
                hit = testfairy.Land(platform)
                if hit == True:
                    #print(platform.rect)
                    hit_a_platform = True
            if hit_a_platform == False:
                testfairy.MagicGravity(5)

            if pressed_keys[pygame.K_LEFT]:
                testfairy.move(-5)
            if pressed_keys[pygame.K_RIGHT]:
                testfairy.move(5)

            for item in items:
                item.draw(screen)
            if testfairy.Grab(item):
                if dust in items:
                    pickup_sound.play()
                    scoreboard.score = scoreboard.score + 100

                    item.x = random.randint(200, 600)
                    item.y = random.randint(50, 300)

            scoreboard.draw()
            testfairy.bound()
            testfairy.draw()

        if background == start_background:
            start.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()