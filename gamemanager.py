# game manager
import pygame
from pygame.locals import *

# import the other games
import hangman
import SnakesAndLadders
import Tetrisfinal
# import snake_LH_Git

App = Tetrisfinal.TetrisApp()

# define Colors
white = (242, 225, 194)
blue = (51, 89, 166)
red = (130, 176, 217)

# Load game preview Images
Img_hangman = pygame.image.load("hangman_icon.png")
Img_hangman = pygame.transform.scale(Img_hangman, (90, 130)) # transform to useful size
Img_sal = pygame.image.load("bg.jpg")
Img_sal = pygame.transform.scale(Img_sal, (200, 130))

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

            # keys pressed
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                # App = Tetrisfinal.TetrisApp()
                App.run()
            if keys[K_LEFT]:
                SnakesAndLadders.gameLoop()

        # refresh window
        screen.fill(white)

        # print menu text
        SnakesAndLadders.button("Hangman", 40, 300, 100, 50, red, blue, hangman.main)
        SnakesAndLadders.button("Snakes and Ladders", 150, 300, 200, 50, red, blue, SnakesAndLadders.gameLoop)
        SnakesAndLadders.button("Tetris", 370, 300, 80, 50, red, blue, App.run)
        # SnakesAndLadders.button("Snake", 480, 300, 80, 50, red, blue, snake_LH_Git)
        # print game preview Images
        screen.blit (Img_hangman, (45, 150))
        screen.blit (Img_sal, (150,150))

        # update and tick the Clock
        pygame.display.update()

if __name__ == "__main__":
    main()
