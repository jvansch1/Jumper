import sys, pygame
from screen import Screen
from jumpman import Jumpman
from block import Block

def main():
    pygame.init()
    screen = Screen(1200, 800, (255,255,255))
    screen.display()
    jumpman = Jumpman(screen, 50, 200)
    pygame.display.update()
    block = Block(screen, 50, 50)
    jumpman_x = 50
    jumpman_y = 200
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if jumpman_y < 800 - jumpman.height():
                    jumpman_y = jumpman_y + 10
            if event.key == pygame.K_UP:
                if jumpman_y > 0:
                    jumpman_y = jumpman_y - 10

        screen.screen.fill((255,255,255))
        load_jumpman(screen, jumpman, jumpman_x, jumpman_y)
        handle_block(screen, block)
        print(block.get_x())
        pygame.display.update()

def load_jumpman(screen, jumpman, x,y):
    jumpman.update_x(x)
    jumpman.update_y(y)
    jumpman.display()

def handle_block(screen, block):
    if block and block.get_x() <= 0:
        block.reset_position()
        block.draw()
    else:
        block.draw()

main()
