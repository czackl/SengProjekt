# Hangman
def main():
    import pygame

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
    red = ()
    black = (0,0,0)
    gray = ()
    green = ()

    # Define word list for the game
    words = ["software", "projekt", "informatik", "bingen", "semesterferien", "nudelauflauf", "galgenmann", "minispiel"]

    # Define Alphabet Array
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    currentCharacter = 0

    # define color array for alphabet
    # standard color: black, selected: blue
    # used: grey, correct: green
    colors = []
    for i in range(26):
        colors.append(black)

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
        # refresh game window
        s.fill(white)

        # print character array on screen


        # update an tick the clock
        pygame.display.update()
        clock.tick(FPS)
