#!/usr/bin/python3
"""
Alle Dokumentationskommentare gelten fuer die darauf Folgenden Zeilen:
Importiert die Module um das Spiel spielen zu koennen
"""
import pygame
import random
import gamemanager

# pygame.init()
#Festlegen der Farbe
BG = (255, 255, 255)
FEIND = (0, 0, 0)
"""
Laedt die Bilder fuer die Objekte, legt die Bildgroessen fest und hinterlegt
alles als Variable
"""
#Festlegen der Bilder und der bildgroessen
scale = width, height = 20, 20
sg = pygame.image.load("schlange.png")
sg = pygame.transform.scale(sg, scale)

apl = pygame.image.load("apfel.png")
apl = pygame.transform.scale(apl,scale)

fd = pygame.image.load("fd.png")
fd = pygame.transform.scale(fd,scale)

#Festlegen der Feldgroesse
FELD_B = 600
FELD_H = 600

#Groeße der Kaestchen festlegen
QUADRAT_SEITE = 20

#Anzahl der Feinde festlegen
FEINDE = 3

"""
Legt die Klasse fest, um alle Spielelemente als Kaestchen festzulegen und Sprite liefert
Funktionalitaeten wie beispielsweise eine Kollision
"""
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

    """
    Initialisiert die Randfunktion, die für die "Portale" sorgt
    """
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


"""
Initialisiert das Spielfeld mitsamt Groesse.
snake = [] erschafft ein Array in das spaeter alle gesammelten Kaestchen geschoben werden.
allKaestchen wird geschaffen und erbt von Sprite, damit eine Kollision abgefragt werden kann.
Ebenfalls werden die Feinde dorthin verschoben.
"""
pygame.init()
screen = pygame.display.set_mode([FELD_B, FELD_H])
clock = pygame.time.Clock()

snake = []
allKaestchen = pygame.sprite.Group()
feinde = pygame.sprite.Group()

"""
Erschafft das Kaestchen der Schlange an einem zufaelligen Ort und verschiebt dieses Kaestchen
in die Schlange und auch in allKaestchen
"""
kaestchen = Kaestchen(sg, QUADRAT_SEITE, QUADRAT_SEITE)

#Zufaelligen Startpunkt fuer Schlange finden
kaestchen.rect.x = random.randrange(int(FELD_B / 25)) * 25
kaestchen.rect.y = random.randrange(int(FELD_H / 25)) * 25

snake.append(kaestchen)
allKaestchen.add(kaestchen)

"""
Erschafft das Kaestchen des Apfels an einem zufaelligen Ort und verschiebt dieses Kaestchen
in allKaestchen
"""
#Apfel an zufaelliger Position generieren
apfel = Kaestchen(apl, QUADRAT_SEITE, QUADRAT_SEITE)

apfel.rect.x = random.randrange(int(FELD_B / 25)) * 25
apfel.rect.y = random.randrange(int(FELD_H / 25)) * 25

allKaestchen.add(apfel)

# screen.blit(sg,(kaestchen.rect.x, kaestchen.rect.y))
# screen.blit(apl,(apfel.rect.x, apfel.rect.y))

"""
Generiert die 3 Feinde an zufaelliger Position, belegt diese mit dem zugeorneten
Bild und schiebt die Feinde in allKaestchen.
"""
#Feinde an zufaelliger Position generieren
for index in range(FEINDE):
    feind = Kaestchen(fd, QUADRAT_SEITE, QUADRAT_SEITE)
    feind.rect.x = random.randrange(int(FELD_B / 25)) * 25
    feind.rect.y = random.randrange(int(FELD_H / 25)) * 25
    feinde.add(feind)
    allKaestchen.add(feind)


stop = False

"""
Funktion laedt die Bilder an die aktuelle Position des jeweiligen Kaestchens,
welches sich in allKaestchen befindet.
"""
def print_Bilder(allKaestchen):
    for b in allKaestchen:
        screen.blit(b.bild, (b.rect.x, b.rect.y))

def reset_game_variables():
    global stop
    stop = False

    screen = pygame.display.set_mode([FELD_B, FELD_H])

"""
Wandelt die vorher lokal definierten Variablen in globale um, damit diese auch in der main-Methode funktionieren.
"""
def main():
    global stop
    global snake
    global allKaestchen

    reset_game_variables()


    """
    Ist die Gameloop-Funktion, das solange laeuft, bis die "stop"-Bedingung auf True gesetzt wird.
    Zudem fuehrt die Schleife bei Schliessen des Fensters zurueck zum Gamemanager.
                Steuerung:
                Pfeil-links: Spieler bewegt sich nach links
                Pfeil-rechts: Spieler bewegt sich nach rechts
                Pfeil-hoch: Spieler bewegt sich nach oben
                Pfeil-runter: Spieler bewegt sich nach unten
    """
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


        """
        In den hit_(...)-Abschnitten wird getestet, ob die Schlange auf sich selbst,
        einen Apfel oder einen Feind trifft. Je nachdem werden die gesammelten Elemente
        der Schlange wieder zurueckgesetzt (Schlange trifft Schlange & Schlange trifft Feind)
        oder aber um ein Element verlaengert (Schlange trifft Apfel).
        """
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


        """
        screen.fill definiert den Hintergrund, Print_Bilder bezieht die vorher definierten
        und in der Funktion allKaestchen abgelegten Bilder. Weiterhin werden diese Bilder
        dem jeweiligen Objekt zugeordnet.

        clock.tick definiert die Geschwindigkeit der Schlange
        """
        screen.fill(BG)

        # allKaestchen.draw(screen)
        print_Bilder(allKaestchen)
        pygame.display.flip()

        #9 FPS
        clock.tick(9)

if __name__ == "__main__":
    main()

# pygame.quit()
