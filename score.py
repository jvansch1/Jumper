import pygame

class Score:

    def __init__(self, score, screen):
        self.score = score
        self.screen = screen

    def increment_score(self):
        self.score += 1

    def render(self):
        basic_font = pygame.font.SysFont(None, 48)
        text = basic_font.render('Score: {0}'.format(self.score), True, (255, 0, 0), (255, 255, 255))
        self.screen.screen.blit(text, (100,100))
