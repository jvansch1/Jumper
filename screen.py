import pygame

class Screen:

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        self.screen = pygame.display.set_mode((self.height, self.width))

    def display(self):
        self.screen.fill(self.color)
        pygame.display.flip()

    def update(self):
        self.fill()
        pygame.display.flip()

    def fill(self):
        self.screen.fill(self.color)
