# game manager
import pygame
from pygame.locals import *

# import the other games
import hangman
import SnakesAndLadders
import Tetrisfinal
import snake_LH_Git

App = Tetrisfinal.TetrisApp()

# define Colors
white = (242, 225, 194)
blue = (51, 89, 166)
red = (130, 176, 217)

# Load game preview Images
Img_hangman = pygame.image.load("hangman_icon.png")
Img_hangman = pygame.transform.scale(Img_hangman, (90, 130)) # transform to useful size
Img_sal = pygame.image.load("bg.jpg")
Img_sal = pygame.transform.scale(Img_sal, (210, 130))
Img_snake = pygame.image.load("Snake_Screenshot_cut.png")
Img_snake = pygame.transform.scale(Img_snake, (100, 130))
Img_tetris = pygame.image.load("tetris.png")
Img_tetris = pygame.transform.scale(Img_tetris, (100, 130))

def main():

    #init
    pygame.init()
    width = 640
    height = 480
    screen = pygame.display.set_mode((width, height)) # s for screen
    pygame.display.set_caption("Spielmenue")
    FPS = 30

    # game loop
    running = True
    while running:
        # event loop
        for event in pygame.event.get():

            # exit
            if event.type==pygame.QUIT:
                running = False
                pygame.quit()
                exit(0)

        # refresh window
        screen.fill(white)

        # print menu text
        SnakesAndLadders.button("Hangman", 30, 300, 100, 50, red, blue, hangman.main)
        SnakesAndLadders.button("Snakes and Ladders", 150, 300, 210, 50, red, blue, SnakesAndLadders.gameLoop)
        SnakesAndLadders.button("Tetris", 380, 300, 100, 50, red, blue, App.run)
        SnakesAndLadders.button("Snake", 500, 300, 100, 50, red, blue, snake_LH_Git.main)

        # print game preview Images
        screen.blit (Img_hangman, (45, 150))
        screen.blit (Img_sal, (150,150))
        screen.blit (Img_snake, (500,150))
        screen.blit (Img_tetris, (380,150))

        # update and tick the Clock
        pygame.display.update()

if __name__ == "__main__":
    main()
