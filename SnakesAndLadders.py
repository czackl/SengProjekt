#import moduls, gamemanager
import pygame, random, gamemanager

#init pygame
pygame.init()

#define pitch, screen size
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

#define token radius
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

screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption('Snakes & Ladders')
clock = pygame.time.Clock()

#load background, scale it
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,sizePitch)

def quitGame():
    #run gamemanager, post QUIT-event in Pygames Event-Queue
    gamemanager.main()
    pygame.event.post(pygame.event.Event(pygame.QUIT))

def background():
    #blit background image
    screen.blit(bg,(0,0))

def resetGame():
    #reset all valuables
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
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def win(pT, color):
    pygame.time.wait(400)
    screen.fill(oliveGreen)
    playerWinText = pygame.font.Font('freesansbold.ttf',50)
    textSurf, textRect = textObjects(pT, playerWinText, color)
    textRect.center = ((400),(150))
    screen.blit(textSurf, textRect)
    winText = pygame.font.Font('freesansbold.ttf',50)
    textSurf, textRect = textObjects("you won", winText, color)
    textRect.center = ((400),(250))
    screen.blit(textSurf, textRect)
    pygame.display.update()
    pygame.time.wait(5000)
    resetGame()
    gamemanager.main()

def playerText(pT, color):
    playerText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = textObjects(pT, playerText, color)
    textRect.center = ((700),(150))
    screen.blit(textSurf, textRect)

def turnText():
    turnText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = textObjects("it´s your turn", turnText, black)
    textRect.center = ((700),(200))
    screen.blit(textSurf, textRect)

def biteText():
    biteText = pygame.font.Font('freesansbold.ttf',22)
    textSurf, textRect = textObjects("A snake bites you!", biteText, brightRed)
    textRect.center = ((700),(80))
    screen.blit(textSurf, textRect)

def ladderText():
    ladderText = pygame.font.Font('freesansbold.ttf',22)
    textSurf, textRect = textObjects("There´s a ladder!", ladderText, brightRed)
    textRect.center = ((700),(100))
    screen.blit(textSurf, textRect)

def button(text,x,y,w,h,mouseOn,mouseOff,action=None):
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
    global diceNum, turn, move

    diceNum = random.randint(1,6)

    move = True

    if turn:
        turn = False
    else:
        turn = True
    pygame.time.wait(1000)

    return diceNum

def reset_diplay():
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
        pygame.time.wait(3000)

    return switchSnakes.get(playerPosition, playerPosition)

def ladders(playerPosition):
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
        pygame.time.wait(3000)

    return switchLadders.get(playerPosition, playerPosition)

def gameLoop():
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

        if diceNum != 0:
            diceText = pygame.font.Font("freesansbold.ttf",24)
            textSurf, textRect = textObjects(str(diceNum), diceText, black)
            textRect.center = ( (700), (325) )
            screen.blit(textSurf, textRect)

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

        if (player1Position[1] == 20)  & (player1Position[0] == 30) | (player1Position[1] < 20):
            win(player1Text, lawnGreen)

        if (player2Position[1] == 20)  & (player2Position[0] == 30) | (player2Position[1] < 20):
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
                    quitGame()

if __name__ =="__main__":
    gameLoop()
