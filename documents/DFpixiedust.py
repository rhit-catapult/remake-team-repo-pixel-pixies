import pygame
import sys
import random
import math
pygame.init()

def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dahlia's Flight")
    clock = pygame.time.Clock()
    image1 = pygame.image.load("pixiedust.png")
    dust = pixiedust(image1, random.randint(25,775),550)
    # pickup_sound = pygame.mixer.Sound("pickupPD.wav")
    WHITE = pygame.Color("white")
    BLACK = pygame.Color("black")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(WHITE)
        dust.draw(screen)
        pygame.display.update()


        #if event.type ==  # hero hits pixdust
        # pickup_sound.play()
        # def hit(self):
        #     if hero



class pixiedust:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.image = pygame.transform.scale(self.image, (75, 50))

main()


