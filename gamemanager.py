# game manager
import pygame
from pygame.locals import *

# import the other games
import hangman

def main():
    #init
    pygame.init()
    width = 640
    height = 480
    s = pygame.display.set_mode((width, height)) # s for screen
    pygame.display.set_caption("Spielmenue")
    FPS = 30

    # define Colors
    white = (255,255,255)

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

        # refresh window
        s.fill(white)

        # print menu text

        # update and tick the Clock
        pygame.display.update()

if __name__ == "__main__":
    main()
