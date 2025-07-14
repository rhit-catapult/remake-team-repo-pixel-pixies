import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dahlia's Flight")
    clock = pygame.time.Clock()
    image1 = pygame.image.load("pixiedust.png")
    pickup_sound = pygame.mixer.Sound("pickupPD.wav")
    IMAGE_SIZE = 50
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
    pygame.init()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((WHITE))
        pygame.display.update()

class pixiedust:
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.pixiedust, (self.x, self.y))

# def hit(self):
#     if hero

# while True:
    # for event in pygame.event.get():
        # if event.type == #hero hits pixdust
        #     pickup_sound.play()
    # screen.blit(image1, (0, 0))
    pygame.display.update()

main()

