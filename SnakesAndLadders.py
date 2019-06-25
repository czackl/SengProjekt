import pygame, random

pygame.init()

sizePitch = width, height = 600, 400
sizeScreen = width, height = 800, 400
#Feld "Steuerung" von x1=600 bis x2=800 height = 400

black = 0,0,0
magenta = 255,0,255
white = 255,255,255
red = (200,0,0)
green = (0,200,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)

srad = 15

diceNum = 0

screen = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption('Snakes & Ladders')
clock = pygame.time.Clock()


bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,sizePitch)

def quitGame():
    pygame.event.post(pygame.event.Event(pygame.QUIT))

def background():
    screen.blit(bg,(0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(text,x,y,w,h,mouseOn,mouseOff,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, mouseOn,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, mouseOff,(x,y,w,h))

    buttonText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(text, buttonText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def turnText():
    turnText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = text_objects("It´s your turn", turnText)
    textRect.center = ((700),(200))
    screen.blit(textSurf, textRect)
    


def rollDice():
    global diceNum

    diceNum = random.randint(1,6)
    print(diceNum)

    diceText = pygame.font.Font("freesansbold.ttf",24)
    textSurf, textRect = text_objects(str(diceNum), diceText)
    textRect.center = ( (700), (325) )
    screen.blit(textSurf, textRect)

    movePlayer1()

xStart = 30
yStart = 380
xNeu = 0
xAlt = xStart
xMax = 570
xMin = 30
xUe = 0
yNeu = 0
yAlt = yStart

player1Position = (xStart, yStart)
player2Position = (xStart, yStart)

def movePlayer1():
    global xNeu, yNeu, xUe, xAlt, yAlt
    if yAlt == 380 or yAlt == 300 or yAlt == 220 or yAlt == 140 or yAlt == 60:
        xNeu = xAlt + (diceNum * 60)
        if xNeu > xMax:
            yNeu = yStart - 40
            xUe = xNeu - xMax
            xNeu = xMax - xUe
        xAlt = xNeu
        xUe = 0
        player1Position = (xNeu, yNeu)
        """if player == player1Position:
            pygame.draw.circle(screen, black, player, srad, 0)
        else:
            pygame.draw.circle(screen, magenta, player, srad, 0)"""
            
    else:
        xNeu = xAlt - (diceNum * 60)
        if xNeu < xMin:
            yNeu = yAlt -40
            xNeu = xNeu * (-1)
        xAlt = xNeu
        xUe = 0
        player1Position = (xNeu, yNeu)
        """if player == player1Positon:
            pygame.draw.circle(screen, black, player, srad, 0)
        else:
            pygame.draw.circle(screen, magenta, player, srad, 0)"""

def gameLoop():
   
    running = 1

    while running:

        clock.tick(15)

        screen.fill(white)

        background()

        #buttons()
        button("DICE!",650,250,100,50,brightGreen,green,rollDice)
        button("Quit",760,380,40,20,brightRed,red,quitGame)

        turnText()

        pygame.display.flip()

        """pygame.draw.circle(screen, black, player1Position, srad, 0)
        pygame.draw.circle(screen, magenta, player2Position, srad, 0)"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_RIGHT:
                    rollDice()
                    movePlayer1()
                    pygame.draw.circle(screen, black, player1Position, srad, 0)
                if event.key == pygame.K_LEFT:
                    rollDice()
                    movePlayer1()
                    pygame.draw.circle(screen, black, player1Position, srad, 0)

        pygame.display.flip()

gameLoop()
pygame.quit()
quit()
    
