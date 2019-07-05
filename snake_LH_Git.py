#!/usr/bin/python3
import pygame
import random
import gamemanager

# pygame.init()
#Festlegen der Farben
BG = (255, 255, 255)
FEIND = (120, 40, 120)

#Festlegen der Bilder und der bildgroeßenc
scale = width, height = 20, 20
sg = pygame.image.load("schlange.png")
sg = pygame.transform.scale(sg, scale)

apl = pygame.image.load("apfel.png")
apl = pygame.transform.scale(apl,scale)

fd = pygame.image.load("apfel.png")
fd = pygame.transform.scale(fd,scale)

#Festlegen der Feldgroeße
FELD_B = 600
FELD_H = 600

#Groeße der Kaestchen festlegen
QUADRAT_SEITE = 20

#Anzahl der Feinde festlegen
FEINDE = 3

#Spielfeld mit Ein- und Austrittsfunktion sowie der Geschwindigkeit initialisieren
class Kaestchen(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(FEIND)
        self.bild = color

        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0


    def update(self):

        if self.rect.x + QUADRAT_SEITE > FELD_B:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = FELD_B - QUADRAT_SEITE - 5
        elif self.rect.y + QUADRAT_SEITE > FELD_H:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = FELD_H - QUADRAT_SEITE - 5
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y

    def changespeed(self, x, y):
        self.change_x = x
        self.change_y = y



pygame.init()
screen = pygame.display.set_mode([FELD_B, FELD_H])
clock = pygame.time.Clock()

snake = []
allKaestchen = pygame.sprite.Group()
feinde = pygame.sprite.Group()

kaestchen = Kaestchen(sg, QUADRAT_SEITE, QUADRAT_SEITE)

#Zufaelligen Startpunkt fuer Schlange finden
kaestchen.rect.x = random.randrange(int(FELD_B / 25)) * 25
kaestchen.rect.y = random.randrange(int(FELD_H / 25)) * 25

snake.append(kaestchen)
allKaestchen.add(kaestchen)

#Apfel an zufaelliger Position generieren
apfel = Kaestchen(apl, QUADRAT_SEITE, QUADRAT_SEITE)

apfel.rect.x = random.randrange(int(FELD_B / 25)) * 25
apfel.rect.y = random.randrange(int(FELD_H / 25)) * 25

allKaestchen.add(apfel)

# screen.blit(sg,(kaestchen.rect.x, kaestchen.rect.y))
# screen.blit(apl,(apfel.rect.x, apfel.rect.y))

#Feinde an zufaelliger Position generieren
for index in range(FEINDE):
    ########################################## sd-> fd
    feind = Kaestchen(sg, QUADRAT_SEITE, QUADRAT_SEITE)
    feind.rect.x = random.randrange(int(FELD_B / 25)) * 25
    feind.rect.y = random.randrange(int(FELD_H / 25)) * 25
    feinde.add(feind)
    allKaestchen.add(feind)


stop = False

def print_Bilder(allKaestchen):
    for b in allKaestchen:
        screen.blit(b.bild, (b.rect.x, b.rect.y))

def reset_game_variables():
    global stop
    stop = False

    screen = pygame.display.set_mode([FELD_B, FELD_H])

def main():
    global stop
    global snake
    global allKaestchen

    reset_game_variables()

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
                gamemanager.main()
            #Steuerung mit den Pfeiltasten definieren
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake[0].change_x != 25:
                    snake[0].changespeed(-25, 0)
                elif event.key == pygame.K_RIGHT and snake[0].change_x != -25:
                    snake[0].changespeed(25, 0)
                elif event.key == pygame.K_UP and snake[0].change_y != 25:
                    snake[0].changespeed(0, -25)
                elif event.key == pygame.K_DOWN and snake[0].change_y != -25:
                    snake[0].changespeed(0, 25)



        #Pruefen ob Schlange auf Feind getroffen ist
        hit_Kaestchen = pygame.sprite.spritecollide(snake[0], feinde, False)

        if hit_Kaestchen:
            for element in snake:
                if element != snake[0]:
                    allKaestchen.remove(element)
                    snake = snake[:1]

        #Pruefen ob Schlange auf sich selbst getroffen ist
        hit_Kaestchen = pygame.sprite.spritecollide(snake[0], snake, False)

        if hit_Kaestchen and len(hit_Kaestchen) > 1:
            for element in snake:
                if element != snake[0]:
                    allKaestchen.remove(element)
                    snake = snake[:1]

        #Pruefen ob Schlange Apfel gefunden hat
        hit_Kaestchen = pygame.sprite.spritecollide(snake[0], [apfel], False)

        newKaestchen = None

        if hit_Kaestchen:
            newKaestchen = Kaestchen(sg, QUADRAT_SEITE, QUADRAT_SEITE)
            newKaestchen.rect.x = snake[-1].rect.x
            newKaestchen.rect.y = snake[-1].rect.y

            snake.append(newKaestchen)
            allKaestchen.add(newKaestchen)

            #Position fuer Apfel erstellen ohne dass diese gleich wie die der Schlange oder der Feinde ist
            while True:
                apfel.rect.x = random.randrange(int(FELD_B / 25)) * 25
                apfel.rect.y = random.randrange(int(FELD_H / 25)) * 25
                hit_Kaestchen = pygame.sprite.spritecollide(apfel, snake, False)
                hit_Kaestchen2 = pygame.sprite.spritecollide(apfel, feinde, False)

                if not hit_Kaestchen and not hit_Kaestchen2:
                    break


        #Anhaengsel zum hinterherlaufen bringen
        for index in range(len(snake) - 1, 0, -1):
            snake[index].rect.x = snake[index - 1].rect.x
            snake[index].rect.y = snake[index - 1].rect.y

        snake[0].update()

        screen.fill(BG)

        # allKaestchen.draw(screen)
        print_Bilder(allKaestchen)
        pygame.display.flip()

        #9 FPS
        clock.tick(9)

if __name__ == "__main__":
    main()

# pygame.quit()
