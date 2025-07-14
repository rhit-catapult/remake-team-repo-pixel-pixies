import pygame
import random


#platforms
class Platforms:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

def draw(self):
    pygame.draw.rect(self.screen, (255,255,255), (10, 3, 3, 2, 2))

Platforms.draw()