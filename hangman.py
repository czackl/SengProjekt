# Hangman
"""
Script for the Hangman Game
"""
import pygame
from pygame.locals import *
import gamemanager
import random

# Init stuff
width = 640
height = 480
pygame.init()
FPS = 30
s = pygame.display.set_mode((width, height)) # s for screen
pygame.display.set_caption("Hangman")

clock = pygame.time.Clock()

# Define Colors
white = (38, 37, 35)
red = (242, 109, 61)
blue = (166, 146, 129)
black = (242, 230, 216)
gray = (166, 98, 38)
green = (204, 29, 23)

# Word collection
words = ["SOFTWARE", "PROJEKT", "INFORMATIK", "BINGEN", "SEMESTERFERIEN",
"NUDELAUFLAUF", "GALGENMANN", "MINISPIEL", "BIOINFORMATIK", "SOMMERFERIEN",
"METAPHER", "KISCHKERNSPUCKEN", "EINFALTSPINSEL", "GALIONSFIGUR", "PORTMONNAIE",
"NICHTSDESTOTROTZ", "ZUCCHINI", "LIZENZIEREN", "ASYMETRIE", "BRILLIANT",
"DELEGATION", "DIPHTHERIE", "DILETTANT", "FLACHBETTSCANNER", "FURNIER",
"GALOPPIEREN", "GINKGO", "GRATWANDERUNG", "INBUSSCHRAUBE", "MOBILIAR",
"OBSOLET", "PAPPENSTIEL", "PERIPHER", "PROJEKTION", "QUARZUHR", "RESSOURCE",
"REVANCHIEREN", "RENTIER", "RHETORIK", "REPARATUR", "REVISION", "REFLEXION",
"SAITE", "SEITE", "SILHOUETTE", "SISYPHUSARBEIT", "SPAGHETTI", "STANDARD",
"TRIUMPHIEREN", "ZARTBESAITET", "VOLLPFOSTEN", "DRAHTESEL", "DOPPELGEMOPPELT",
"DACHSCHADEN", "AKTENORDNER", "BLECHLAWINE", "DONNERWETTER", "DREHWURM",
"DURSTSTRECKE", "EFFEKTHASCHEREI", "FEIERABEND", "FERNWEH", "FILMRISS",
"GABELSTAPLER", "GEISTESBLITZ", "GEISTEFAHER", "GEWISSENSBISS", "HEIMWEH",
"HEISSHUNGER", "HEXENSCHUSS", "HOCHSTAPLER", "KLOBRILLE", "LAMPENFIEBER",
"LEBENSZEIT", "LEITMOTIV", "MIESEPETER", "NARRENFREIHEIT", "OHNMACHT",
"PUTZFIMMEL", "REISSWOLF", "FLEISCHWOLF", "SCHADENFREUDE", "SCHERZKEKS",
"SCHLITZOHR", "SCHLUCKSPECHT", "SCHLUSSLICHT", "SCHLUSSSTRICH", "SOLLBRUCHSTELLE",
"SOMMERSPROSSEN", "SPRITZTOUR", "STERNENHIMMEL", "TUNICHTGUT", "VERSTRICKUNG",
"VORABEND", "VORFREUDE", "VORREITER", "WASSERRATTE", "WORTSCHATZ", "WELTFRIEDEN",
"ZEITLOS", "ZEITLUPE", "ZEITVETREIB", "ZUFLUCHTSORT", "WALDEINSAMKEIT",
"FERNWEH", "HOKUSPOKUS", "KAFFEKLATSCH", "KLATZENJAMMER", "KAULQUAPPE",
"PURZELBAUM", "PUSTEKUCHEN", "SCHAPSIDEE", "TOLLPATSCH", "WACKELDACKEL",
"WIMMELBILD"]
word = ""
cipherword = []

# Define Alphabet Array
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
currentCharacter = 0
colors = [] # array for color of the alphabet

# Load Images
Img_6 = pygame.image.load("hangman_6.png")
Img_5 = pygame.image.load("hangman_5.png")
Img_4 = pygame.image.load("hangman_4.png")
Img_3 = pygame.image.load("hangman_3.png")
Img_2 = pygame.image.load("hangman_2.png")
Img_1 = pygame.image.load("hangman_1.png")
Img_0 = pygame.image.load("hangman_0.png")

lifes = 6

# Methods
def reset_game_variables():
    """
    Method used for resetting all Game Variables before starting a new game.
    """
    # reset the variables for reuse
    global colors
    global word
    global cipherword
    global currentCharacter
    global lifes

    s = pygame.display.set_mode((width, height)) # s for screen
    pygame.display.set_caption("Galgenmaennchen")

    currentCharacter = 0
    lifes = 6

    # standard color: black, selected: blue
    # used: red
    colors = []
    for i in range(26):
        colors.append(black)
    colors[currentCharacter] = green
    # encrypt cipher word
    word = words[random.randint(0, len(words)-1)] # randomly chosen word for the games
    cipherword = []
    for i in range(len(word)):
        cipherword.append("_")

def key_right():
    """
    method used for calculating the picked character from the character list
    red (already used) characters are skipped
    when reaching the rigth edge the "curser" reenters on the left side
    """
    global colors
    global currentCharacter
    if colors[currentCharacter] == green:
        colors[currentCharacter] = black
    currentCharacter +=1
    currentCharacter %= 26
    # if current character is already used
    while colors[currentCharacter] == red:
        currentCharacter += 1
        currentCharacter %= 26
    colors[currentCharacter] = green

def key_left():
    """
    Calculting the chosen character when the left key is pressed
    already used characters are skipped
    """
    global colors
    global currentCharacter
    if colors[currentCharacter] == green:
        colors[currentCharacter] = black
    currentCharacter -= 1
    if currentCharacter < 0:
        currentCharacter = 25
    while colors[currentCharacter] == red:
        currentCharacter -= 1
        if currentCharacter < 0:
            currentCharacter = 25
    colors[currentCharacter] = green

def enter():
    """
    Calculting if the chosen character is in the cipher word when the user presses enter
    """
    global lifes
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
        lifes -= 1

def print_dead_message():
    """
    When the user has no more lifes a dead message is printed
    """
    #print dead message
    pygame.time.wait(400)
    font_obj = pygame.font.SysFont("Comic Sans MS", 100)
    text_obj = font_obj.render("You lost", True, red)
    s.blit(text_obj, (150, 150))
    pygame.display.update()
    pygame.time.wait(1500)
    # back to the menue
    gamemanager.main()

def print_won_message():
    """
    When the user guessed all characters an is not already dead a won message is printed
    """
    #print won message
    pygame.time.wait(400)
    font_obj = pygame.font.SysFont("Comic Sans MS", 100)
    text_obj = font_obj.render("You Won", True, red)
    s.blit(text_obj, (150, 150))
    pygame.display.update()
    pygame.time.wait(1500)
    # back to the menue
    gamemanager.main()

def button(text,x,y,w,h,mouseOn,mouseOff,action=None):
    """
    Method implementing a Button which can be arranged in an pygame window
    Usage: button (text, x, y, w, h, mouseOn, mouseOff, action)
    text: text to be displayed by the button
    x: top left x coordinate
    y: top left y coordinate
    w: width of the button
    h: heigth of the button
    mouseOn: color when hovering the button with the cursor
    mouseOff: standart button colors
    action: method called when pressed, method name without parenthesis
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(s, mouseOn,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(s, mouseOff,(x,y,w,h))

    buttonText = pygame.font.SysFont("comicsansms",20)
    textSurf = buttonText.render(text, 20, white)
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    s.blit(textSurf, textRect)

def main():
    """
    Main method for calling the games
    includes the setup (reset Variables) and the game loop
    """
    pygame.init()
    reset_game_variables()
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
                quit()

            # keys pressed
            keys = pygame.key.get_pressed()
            # rigth key
            if keys[K_RIGHT]:
                key_right()

            # left key
            if keys[K_LEFT]:
                key_left()

            # enter
            if keys[K_RETURN]:
                enter()

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
        cipherxmax = width- 40
        cipherCharacterSpace = 25
        font_obj = pygame.font.SysFont("Comic Sans MS", 25)

        for i in range (len(cipherword)-1, -1, -1):
            text_obj = font_obj.render(cipherword[i], True, black)
            s.blit(text_obj, (cipherxmax, 200))
            cipherxmax -= cipherCharacterSpace

        # print hangman image on screen; image size: 170, 220, start coordinates 20,100
        # pygame.draw.rect(s, blue, (20,100, 170,220))
        img_x = 30
        img_y = 130
        if lifes == 6:
            s.blit(Img_6, (img_x,img_y))
        elif lifes == 5:
            s.blit(Img_5, (img_x,img_y))
        elif lifes == 4:
            s.blit(Img_4, (img_x,img_y))
        elif lifes == 3:
            s.blit(Img_3, (img_x,img_y))
        elif lifes == 2:
            s.blit(Img_2, (img_x,img_y))
        elif lifes == 1:
            s.blit(Img_1, (img_x,img_y))
        elif lifes == 0:
            s.blit(Img_0, (img_x,img_y))
            print_dead_message()
        else:
            s.blit(Img_0, (img_x,img_y))
            print_dead_message()

        # Print menu bar
        pygame.draw.rect(s, blue, (0,0, width, 30))

        # Print Buttons
        button ("Back", 0, 0, 50, 30, red, blue, gamemanager.main)
        button ("Reset", 55, 0, 70, 30, red, blue, reset_game_variables)
        button ("Left: <    Right: >    Choose: Enter", 380, 0, 200, 30, blue, blue)

        # test if player has won or lost
        if "_" not in cipherword:
            running = False
            print_won_message()

        # update an tick the clock
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
