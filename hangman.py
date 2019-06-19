# Hangman
import pygame
from pygame.locals import *
import gamemanager
import random

def main():
    # init
    pygame.init()
    width = 640
    height = 480
    s = pygame.display.set_mode((width, height)) # s for screen
    pygame.display.set_caption("Galgenmaennchen")
    FPS = 30

    clock = pygame.time.Clock()

    # Define Colors
    white = (255,255,255)
    red = (255, 0, 0)
    blue = (0,0,255)
    black = (0,0,0)
    gray = ()
    green = (0, 255, 0)

    # Define word list for the game
    words = ["software", "projekt", "informatik", "bingen", "semesterferien", "nudelauflauf", "galgenmann", "minispiel", "sengsationell", "photosynthese", "desoxyribonukleinsaeure"]
    word = words[random.randint(0, len(words))] # randomly chosen word for the games
    cipherword = []
    for i in range(len(word)):
        cipherword.append("_")

    # Define Alphabet Array
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    currentCharacter = 0

    # define color array for alphabet
    # standard color: black, selected: blue
    # used: red
    colors = []
    for i in range(26):
        colors.append(black)
    colors[i] = blue

    #######################
    # game loop
    #######################
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
            # rigth key
            if keys[K_RIGHT]:
                if colors[currentCharacter] == blue:
                    colors[currentCharacter] = black
                currentCharacter +=1
                currentCharacter %= 26
                # if current character is already used
                while colors[currentCharacter] == red:
                    currentCharacter += 1
                    currentCharacter %= 26
                colors[currentCharacter] = blue
            # left key
            if keys[K_LEFT]:
                if colors[currentCharacter] == blue:
                    colors[currentCharacter] = black
                currentCharacter -= 1
                if currentCharacter < 0:
                    currentCharacter = 25
                while colors[currentCharacter] == red:
                    currentCharacter -= 1
                    if currentCharacter < 0:
                        currentCharacter = 25
                colors[currentCharacter] = blue
            # enter
            if keys[K_RETURN]:
                # check if key in word
                character = alphabet[currentCharacter]
                colors[currentCharacter] = red
                # check if character in word
                if character in word:
                    # character is in word
                    for c in range (len(word)):
                        if word[c] == (character):
                            cipherword[c] = character
                    # print succes message

                else:
                    # character is not in word
                    # print "no succes" message
                    pass


        # refresh game window
        s.fill(white)

        # print character array on screen
        alphabetx = 10
        alphabetwidth = width /len(alphabet)
        font_obj = pygame.font.SysFont("Comic Sans MS", 15)

        for i in range (26):
            text_obj = font_obj.render(alphabet[i], True, colors[i])
            s.blit(text_obj, (alphabetx,450))
            alphabetx += alphabetwidth

        # print cipher word on screen
        cipherx = 450
        cipherCharacterSpace = 25
        font_obj = pygame.font.SysFont("Comic Sans MS", 25)

        for i in range (len(cipherword)):
            text_obj = font_obj.render(cipherword[i], True, black)
            s.blit(text_obj, (cipherx, 200))
            cipherx += cipherCharacterSpace

        # test if player has won or lost
        if "_" not in cipherword:
            running = False

            #print won message
            pygame.time.wait(300)
            s.fill(white)
            font_obj = pygame.font.SysFont("Comic Sans MS", 100)
            text_obj = font_obj.render("You Won", True, red)
            s.blit(text_obj, (150, 150))
            pygame.display.update()
            pygame.time.wait(1000)
            # back to the menue
            gamemanager.main()

        # update an tick the clock
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
