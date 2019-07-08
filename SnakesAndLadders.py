#SnakesAndLadders
"""
Skript for the Snakes and Ladders game
"""
#import moduls, gamemanager
import pygame, random, gamemanager

#init pygame
pygame.init()

#define pitch/screen size
sizePitch = width, height = 600, 400
sizeScreen = width, height = 800, 400

#define colors in rgb-code
black = 0,0,0
lawnGreen = 124,252,0
marineBlue = 0,0,128
oliveGreen = 110,139,61
red = 200,0,0
green = 0,200,0
blue = 0,0,200
brightRed = 255,0,0
brightGreen = 0,255,0
brightBlue = 0,0,255

#define token radius/diceNum
srad = 15
diceNum = 0

#define booleans
move = False
turn = False
snake = False
ladder = False

#define player text
player1Text = "Player1"
player2Text = "Player2"

#set screen to right size/ display caption, define clock
screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption('Snakes & Ladders')
clock = pygame.time.Clock()

#load background, scale it
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,sizePitch)

def quitGame():
    """
    When player wants to quit the Snakes and Ladders Game this methode used
    to jump in the Gamemanager Main and post a QUIT-Event in the Event-Queue
    to quit the Snakes and Ladders game.
    """
    gamemanager.main()
    pygame.event.post(pygame.event.Event(pygame.QUIT))

def background():
    """
    Methode to blit the background image.
    """
    screen.blit(bg,(0,0))

def resetGame():
    """
    Methode used for resetting all game variables, used when player wants to
    play a new game.
    """
    global diceNum, xStart, yStart, xNew, yNew, xMax, xMin, xOv, move, turn, player1Position, player2Position

    xStart = 30
    yStart = 380
    xNew = 0
    yNew = 0
    xMax = 570
    xMin = 30
    xOv = 0
    player1Position = (xStart, yStart)
    player2Position = (xStart, yStart)
    move = False
    turn = False

def textObjects(text, font, color):
    """
    Method used for creating Text Objects.
    text = text
    font = font
    color = color
    """
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def win(pT, color):
    """
    This Method fill the hole screen with one color and blit wich Player
    has won.
    """
    pygame.time.wait(400)
    screen.fill(oliveGreen)
    playerWinText = pygame.font.SysFont("comicsansms",50)
    textSurf, textRect = textObjects(pT, playerWinText, color)
    textRect.center = ((400),(150))
    screen.blit(textSurf, textRect)
    winText = pygame.font.SysFont("comicsansms",50)
    textSurf, textRect = textObjects("you won", winText, color)
    textRect.center = ((400),(250))
    screen.blit(textSurf, textRect)
    pygame.display.update()
    pygame.time.wait(5000)
    resetGame()
    gamemanager.main()

def playerText(pT, color):
    """
    Method that blit the Player who is next.
    pT = wich player text
    color = wich color
    """
    playerText = pygame.font.SysFont("comicsansms",30)
    textSurf, textRect = textObjects(pT, playerText, color)
    textRect.center = ((700),(150))
    screen.blit(textSurf, textRect)

def turnText():
    """
    Method that blit the "it´s your turn" text.
    """
    turnText = pygame.font.SysFont("comicsansms",30)
    textSurf, textRect = textObjects("it´s your turn", turnText, black)
    textRect.center = ((700),(200))
    screen.blit(textSurf, textRect)

def biteText():
    """
    Text method that is blitted if a player is at a position of a snake.
    """
    biteText = pygame.font.SysFont("comicsansms",22)
    textSurf, textRect = textObjects("A snake bites you!", biteText, brightRed)
    textRect.center = ((700),(80))
    screen.blit(textSurf, textRect)

def ladderText():
    """
    Text Methode that is blitted if a Player is at a position of a ladder.
    """
    ladderText = pygame.font.SysFont("comicsansms",22)
    textSurf, textRect = textObjects("There´s a ladder!", ladderText, brightRed)
    textRect.center = ((700),(100))
    screen.blit(textSurf, textRect)

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
        pygame.draw.rect(screen, mouseOn,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, mouseOff,(x,y,w,h))

    buttonText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = textObjects(text, buttonText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def rollDice():
    """
    Method used to create a random integer between 1 and 6 and return it.
    If player roll the dice the boolean "move" get TRUE.
    The boolean "turn" switch from FALSE to TRUE.
    """
    global diceNum, turn, move

    diceNum = random.randint(1,6)

    move = True

    if turn:
        turn = False
    else:
        turn = True
    pygame.time.wait(1000)

    return diceNum

def diceText():
    """
    Method used to show the player wich number he rolled with the dice.
    """
    if diceNum != 0:
        diceText = pygame.font.SysFont("comicsansms",24)
        textSurf, textRect = textObjects(str(diceNum), diceText, black)
        textRect.center = ( (700), (325) )
        screen.blit(textSurf, textRect)


def reset_diplay():
    """
    Reset the display size used used if player changes from gamemanager to
    Snakes and Ladders Game.
    """
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Snakes & Ladders')

xStart = 30
yStart = 380
xNew = 0
yNew = 0
xMax = 570
xMin = 30
xOv = 0
player1Position = (xStart, yStart)
player2Position = (xStart, yStart)

def movePlayer(playerPosition):
    """
    Calculate the new Position for token and return it.
    """
    global diceNum, xStart, yStart, xNew, yNew, xMax, xMin, xOv

    xOld = playerPosition[0]
    yOld = playerPosition[1]

    if move:
        if(yOld % 80 == 60):
            xNew = xOld + (diceNum * 60)
            yNew = yOld
            if xNew > xMax:
                yNew = yOld - 40
                xOv = xNew - xMax
                xNew = xMax - (xOv - 60)

                xOld = xNew
                yOld = yNew
                xOv = 0
                playerPosition = (xNew, yNew)
        else:
            xNew = xOld - (diceNum * 60)
            yNew = yOld
        if xNew < xMin:
            yNew = yOld - 40
            xNew = xNew * (-1)

        xOld = xNew
        yOld = yNew
        xOv = 0
    playerPosition = (xOld, yOld)

    return playerPosition

def snakes(playerPosition):
    """
    Method has a "switch case" for positions of snakes.
    If position switch this method print the bite text and draw the
    token at the new position. Also return the new position.
    """
    switchSnakes = {
        (450 , 380): (210 , 380),
        (150 , 340): (30, 380),
        (330, 300): (570, 380),
        (90, 260): (270, 380),
        (570, 180): (330, 380),
        (390, 180): (270, 260),
        (270, 180): (30, 380),
        (30, 180): (150, 300),
        (330, 100): (450, 300),
        (150, 60): (270, 220),
        (270, 60): (90, 180),
        (570, 60): (450, 220),
        (510, 20): (270, 300),
        (210, 20): (390, 60),
        (90, 20): (150, 140)
    }
    if playerPosition in switchSnakes:
        biteText()
        pygame.draw.circle(screen, lawnGreen, player1Position, srad, 0)
        pygame.draw.circle(screen, marineBlue, player2Position, srad, 0)
        pygame.display.update()
        pygame.time.wait(2500)

    return switchSnakes.get(playerPosition, playerPosition)

def ladders(playerPosition):
    """
    Method has a "switch case" for positions of ladders.
    If position switch this methode print the ladder text and draw the
    token at the new position. Also return the new position.
    """
    switchLadders = {
        (150, 380): (30, 340),
        (330, 380): (390, 340),
        (570, 340): (450, 300),
        (330, 340): (390, 260),
        (210, 340): (390, 100),
        (90, 300): (210, 260),
        (150, 260): (90, 180),
        (510, 220): (390, 140),
        (210, 180): (270, 100),
        (30, 140): (150, 100),
        (450, 100): (330, 60),
        (30, 60): (150, 20),
        (450, 60): (570, 20)
    }
    if playerPosition in switchLadders:
        ladderText()
        pygame.draw.circle(screen, lawnGreen, player1Position, srad, 0)
        pygame.draw.circle(screen, marineBlue, player2Position, srad, 0)
        pygame.display.update()
        pygame.time.wait(2500)

    return switchLadders.get(playerPosition, playerPosition)

def gameLoop():
    """
    Main method for calling the game. Using all methods and set the frames
    per second to 30. The method also init the Event-Queue.
    """
    global move, turn, player1Position, player2Position

    reset_diplay()

    running = 1

    while running:

        clock.tick(30)

        screen.fill(oliveGreen)

        background()

        button("DICE!",650,250,100,50,brightGreen,green,rollDice)
        button("Quit",740,370,60,30,brightRed,red,quitGame)
        button("Reset",600,370,60,30,brightBlue,blue,resetGame)

        turnText()
        diceText()

        if turn:
            player1Position = movePlayer(player1Position)
            playerText(player2Text, marineBlue)
            player1Position = snakes(player1Position)
            player1Position = ladders(player1Position)

        else:
            player2Position = movePlayer(player2Position)
            playerText(player1Text, lawnGreen)
            player2Position = snakes(player2Position)
            player2Position = ladders(player2Position)

        if player1Position == player2Position:
            if turn:
                player2Position = (xStart, yStart)
            else:
                player1Position = (xStart, yStart)

        pygame.draw.circle(screen, lawnGreen, player1Position, srad, 0)
        pygame.draw.circle(screen, marineBlue, player2Position, srad, 0)

        if (player1Position[1] == 20) and (player1Position[0] == 30) or (player1Position[1] < 20):
            win(player1Text, lawnGreen)

        if (player2Position[1] == 20)  and (player2Position[0] == 30) or (player2Position[1] < 20):
            win(player2Text, marineBlue)

        move = False
        snake = False
        ladder = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #if player press esc quitGame()
                    quitGame()

if __name__ =="__main__":
    gameLoop()
