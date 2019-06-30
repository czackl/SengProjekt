import pygame, random, gamemanager

pygame.init()

sizePitch = width, height = 600, 400
sizeScreen = width, height = 800, 400
#Feld "Steuerung" von x1=600 bis x2=800 height = 400

#Colors:
black = 0,0,0
magenta = 255,0,255
oliveGreen = 110,139,61
red = 200,0,0
green = 0,200,0
blue = 0,0,200
brightRed = 255,0,0
brightGreen = 0,255,0
brightBlue = 0,0,255

srad = 15
diceNum = 0

move = False
turn = False
snake = False
ladder = False

player1Text = "Player1"
player2Text = "Player2"

screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption('Snakes & Ladders')
clock = pygame.time.Clock()

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,sizePitch)

def quitGame():
    #Ein QUIT-Event wird in Pygames Event-Warteschlange gepostet.
    gamemanager.main()
    pygame.event.post(pygame.event.Event(pygame.QUIT))

def background():
    screen.blit(bg,(0,0))

def resetGame():
    global diceNum, xStart, yStart, xNeu, yNeu, xMax, xMin, xUe, move, turn, player1Position, player2Position

    xStart = 30
    yStart = 380
    xAlt = xStart
    yAlt = yStart
    xNeu = 0
    yNeu = 0
    xMax = 570
    xMin = 30
    xUe = 0
    player1Position = (xStart, yStart)
    player2Position = (xStart, yStart)
    move = False
    turn = False

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def win(pT):
    pygame.time.wait(400)
    screen.fill(oliveGreen)
    playerWinText = pygame.font.Font('freesansbold.ttf',50)
    textSurf, textRect = text_objects(pT, playerWinText, red)
    textRect.center = ((400),(150))
    screen.blit(textSurf, textRect)
    winText = pygame.font.Font('freesansbold.ttf',50)
    textSurf, textRect = text_objects("you won", winText, red)
    textRect.center = ((400),(250))
    screen.blit(textSurf, textRect)
    pygame.display.update()
    pygame.time.wait(5000)
    gamemanager.main()

def playerText(pT, color):
    playerText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = text_objects(pT, playerText, color)
    textRect.center = ((700),(150))
    screen.blit(textSurf, textRect)

def turnText():
    turnText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = text_objects("it´s your turn", turnText, black)
    textRect.center = ((700),(200))
    screen.blit(textSurf, textRect)

def biteText():
    biteText = pygame.font.Font('freesansbold.ttf',17)
    textSurf, textRect = text_objects("you have been bitten", biteText, brightRed)
    textRect.center = ((700),(200))
    screen.blit(textSurf, textRect)

def ladderText():
    ladderText = pygame.font.Font('freesansbold.ttf',17)
    textSurf, textRect = text_objects("you have found a ladder", ladderText, brightRed)
    textRect.center = ((700),(200))
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
    textSurf, textRect = text_objects(text, buttonText, black)
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
xNeu = 0
yNeu = 0
xMax = 570
xMin = 30
xUe = 0
player1Position = (xStart, yStart)
player2Position = (xStart, yStart)

def movePlayer(playerPosition):
    global diceNum, xStart, yStart, xNeu, yNeu, xMax, xMin, xUe

    xAlt = playerPosition[0]
    yAlt = playerPosition[1]

    if move:
        if(yAlt % 80 == 60):
            xNeu = xAlt + (diceNum * 60)
            yNeu = yAlt
            if xNeu > xMax:
                yNeu = yAlt - 40
                xUe = xNeu - xMax
                xNeu = xMax - (xUe - 60)

                xAlt = xNeu
                yAlt = yNeu
                xUe = 0
                playerPosition = (xNeu, yNeu)
        else:
            xNeu = xAlt - (diceNum * 60)
            yNeu = yAlt
        if xNeu < xMin:
            yNeu = yAlt -40
            xNeu = xNeu * (-1)

        xAlt = xNeu
        yAlt = yNeu
        xUe = 0
    playerPosition = (xAlt, yAlt)

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
        snake = True
        biteText()
        pygame.draw.circle(screen, black, player1Position, srad, 0)
        pygame.draw.circle(screen, magenta, player2Position, srad, 0)
        pygame.display.update()
        pygame.time.wait(3000)

    return switchSnakes.get(playerPosition, playerPosition)

def ladders(playerPosition):
    #(3 : 20) (6 : 14) (11 : 28) (15 : 34) (17 : 74) (22 : 37)
    # (38 : 59) (49 : 67) (57 : 76) (61 : 78) (73 : 86) (81 : 98) (88 : 91)
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
        ladder = True
        ladderText()
        pygame.draw.circle(screen, black, player1Position, srad, 0)
        pygame.draw.circle(screen, magenta, player2Position, srad, 0)
        pygame.display.update()
        pygame.time.wait(3000)

    return switchLadders.get(playerPosition, playerPosition)

def gameLoop():
    global move, turn, snake, ladder, player1Position, player2Position

    reset_diplay()

    running = 1

    while running:

        clock.tick(30)

        screen.fill(oliveGreen)

        background()

        button("DICE!",650,250,100,50,brightGreen,green,rollDice)
        button("Quit",740,370,60,30,brightRed,red,quitGame)
        button("Reset",600,370,60,30,brightBlue,blue,resetGame)

        #turnText()

        if diceNum != 0:
            diceText = pygame.font.Font("freesansbold.ttf",24)
            textSurf, textRect = text_objects(str(diceNum), diceText, black)
            textRect.center = ( (700), (325) )
            screen.blit(textSurf, textRect)

        if turn:
            player1Position = movePlayer(player1Position)
            playerText(player2Text, magenta)
            player1Position = snakes(player1Position)
            player1Position = ladders(player1Position)

        else:
            player2Position = movePlayer(player2Position)
            playerText(player1Text, black)
            player2Position = snakes(player2Position)
            player2Position = ladders(player2Position)

        if player1Position == player2Position:
            if turn:
                player2Position = (xStart, yStart)
            else:
                player1Position = (xStart, yStart)

        if snake == False & ladder == False:
            turnText()

        pygame.draw.circle(screen, black, player1Position, srad, 0)
        pygame.draw.circle(screen, magenta, player2Position, srad, 0)

        if (player1Position[1] == 20)  & (player1Position[0] == 30) | (player1Position[1] < 20):
            win(player1Text)

        if (player2Position[1] == 20)  & (player2Position[0] == 30) | (player2Position[1] < 20):
            win(player2Text)

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
