import pygame
import sys

# player = pygame.transform.scale(pygame.image.load('Fairy.png'),(800,600))

class Platforms:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 100, 40))

    def too_close(self):
        if self.x > self.screen.get_width():
            return True
        if self.y > self.screen.get_height():
            return True
        return False

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Platforms Only")
    screen = pygame.display.set_mode((735, 415))

    test = Platforms(screen, 0, 600)
    my_platform = []
    platform_positions = [(50, 100),
                          (150, 200),
                          (300, 300)]
    for x,y in platform_positions:
        # new_platforms = Platforms(screen,random.randint(0, screen.get_width() - 180),
        #                           random.randint(150, screen.get_height()-40))
        new_platforms = Platforms(screen, x, y)
        my_platform.append(new_platforms)
    while True:
        screen.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Getting coordinates for platforms
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                print(click_position)

        test.draw()
        for platform in my_platform:
            platform.draw()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()





