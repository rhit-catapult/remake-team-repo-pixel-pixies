# import pygame
# import sys
#
# # player = pygame.transform.scale(pygame.image.load('Fairy.png'),(800,600))
#
# class Platforms:
#     def __init__(self, screen, x, y):
#         self.screen = screen
#         self.x = x
#         self.y = y
#
#     def draw(self):
#         pygame.draw.rect(self.screen, (86, 63, 43), (self.x, self.y, 100, 30))
#
#     def too_close(self):
#         if self.x > self.screen.get_width():
#             return True
#         if self.y > self.screen.get_height():
#             return True
#         return False
#
# def main():
#     IMAGE_SIZE1 = 735
#     IMAGE_SIZE2 = 415
#
#     pygame.init()
#     screen = pygame.display.set_mode((IMAGE_SIZE1, IMAGE_SIZE2))
#     image1 = pygame.image.load("Background.jpg")
#     image1 = pygame.transform.scale(image1, (IMAGE_SIZE1, IMAGE_SIZE2))
#
#     clock = pygame.time.Clock()
#     pygame.display.set_caption("Testing the Platforms Only")
#
#     test = Platforms(screen, 10, 375)
#     my_platform = []
#     platform_positions = [(415, 62),
#                           (150, 160),
#                           (345, 300),
#                           (590, 207)]
#
#     for x,y in platform_positions:
#         # new_platforms = Platforms(screen,random.randint(0, screen.get_width() - 180),
#         #                           random.randint(150, screen.get_height()-40))
#         new_platforms = Platforms(screen, x, y)
#         my_platform.append(new_platforms)
#
#     while True:
#         screen.fill((255, 255, 255))
#         screen.blit(image1, (0, 0))
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         #Getting coordinates for platforms
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 click_position = event.pos
#                 print(click_position)
#
#         test.draw()
#         for platform in my_platform:
#             platform.draw()
#         pygame.display.update()
#
#
# # Testing the classes
# if __name__ == "__main__":
#     main()



import pygame
import sys

# Initialize Pygame
pygame.init()

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == MAIN_SCREEN and shape_rect.collidepoint(event.pos):
                current_screen = SECOND_SCREEN

    # Render based on the current screen
    if current_screen == MAIN_SCREEN:
        pygame.draw.rect(screen, BLUE, shape_rect)
    elif current_screen == SECOND_SCREEN:
        screen.fill(GREEN)  # Fill the screen with green for the second screen

    pygame.display.flip()

pygame.quit()
sys.exit()
