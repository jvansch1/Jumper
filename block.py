import pygame
from random import *

class Block:

    def __init__(self, screen, height, width):
        self.screen = screen
        self.height = height
        self.width = width
        self.x = 1200
        self.y = randint(0, 800)

    def draw(self):
        self.update_x()
        pygame.draw.rect(self.screen.screen, (0,0,0), (self.x, self.y, self.width, self.height), 0)

    def update_x(self):
        self.x = float(self.x) - 15

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def reset_position(self):
        self.x = 1200
        self.y = randint(0, 800)
