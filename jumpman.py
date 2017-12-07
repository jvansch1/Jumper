import pygame

class Jumpman():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.file = pygame.image.load('resources/images/mario.png')
        self.x = x
        self.y = y

    def display(self):
        self.screen.screen.blit(self.file, (self.x,self.y))

    def get_height(self):
        return self.file.get_height()

    def get_width(self):
        return self.file.get_width()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update_x(self, x):
        self.x = x

    def update_y(self, y):
        self.y = y
