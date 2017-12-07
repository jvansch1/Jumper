import sys, pygame
from screen import Screen
from jumpman import Jumpman
from block import Block
from score import Score

def main():
    pygame.init()
    screen = Screen(1200, 800, (255,255,255))
    screen.display()
    jumpman = Jumpman(screen, 50, 200)
    pygame.display.update()
    block = Block(screen, 50, 50)
    jumpman_x = 50
    jumpman_y = 200
    score = Score(0, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if jumpman_y < 800 - jumpman.get_height():
                    jumpman_y = jumpman_y + 10
            if event.key == pygame.K_UP:
                if jumpman_y > 0:
                    jumpman_y = jumpman_y - 10

        screen.screen.fill((255,255,255))
        score.render()
        load_jumpman(screen, jumpman, jumpman_x, jumpman_y)
        handle_block(screen, block, score)
        check_for_collision(jumpman, block)
        pygame.display.update()

def load_jumpman(screen, jumpman, x,y):
    jumpman.update_x(x)
    jumpman.update_y(y)
    jumpman.display()

def handle_block(screen, block, score):
    if block and block.get_x() <= 0:
        block.reset_position()
        block.draw()
        score.increment_score()
    else:
        block.draw()

def check_for_collision(jumpman, block):
    block_min_y = block.get_y()
    block_max_y = block.get_y() + block.get_height()

    block_min_x = block.get_x()
    block_max_x = block.get_x() + block.get_width()

    jumpman_min_x = jumpman.get_x()
    jumpman_max_x = jumpman.get_x() + jumpman.get_width()
    jumpman_min_y = jumpman.get_y()
    jumpman_max_y = jumpman.get_y() + jumpman.get_height()

    if ((block_min_y > jumpman_min_y) and (block_max_y < jumpman_max_y)) and (block_min_x < jumpman_min_x + 75):
        print("Collision")




main()
