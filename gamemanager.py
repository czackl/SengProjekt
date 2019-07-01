# game manager
import pygame
from pygame.locals import *

# import the other games
import hangman
import SnakesAndLadders

# define Colors
white = (255,255,255)
blue = (0, 0, 255)
red = (255, 0, 0)


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
                hangman.main()
            if keys[K_LEFT]:
                SnakesAndLadders.gameLoop()

        # refresh window
        screen.fill(white)

        # print menu text
        SnakesAndLadders.button("Hangman", width/2, 50, 100, 50, red, blue, hangman.main)
        SnakesAndLadders.button("Snakes and Ladders", width/2, 100, 200, 50, red, blue, SnakesAndLadders.gameLoop)
        # update and tick the Clock
        pygame.display.update()

if __name__ == "__main__":
    main()
