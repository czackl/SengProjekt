#!/usr/bin/python3
import pygame
import random

K = (0, 0, 0)
BG = (230, 255, 230)
SNAKE = (127, 96, 51)
APPLE = (255, 40, 0)

FELD_H = 800
FELD_B = 800
QUADRAT_S_L = 20

class Kaestchen(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def update(self):
        if self.rect.x + QUADRAT_S_L > FELD_B:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = FELD_B - QUADRAT_S_L - 5
        elif self.rect.y + QUADRAT_S_L > FELD_B:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = FELD_H - QUADRAT_S_L - 5
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y


    def changeSpeed(self, x, y):
        self.change_x = x
        self.change_y = y

pygame.init()

snake = []
allKaestchen = pygame.sprite.Group()

kaestchen = Kaestchen(K, QUADRAT_S_L, QUADRAT_S_L)
kaestchen.rect.x = random.randrange(int(FELD_B/25))*25
kaestchen.rect.y = random.randrange(int(FELD_H/25))*25

snake.append(kaestchen)
allKaestchen.add(kaestchen)


feld = pygame.display.set_mode ([FELD_B, FELD_H])
clock = pygame.time.Clock()


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake[0].changeSpeed(0, -25)
            elif event.key == pygame.K_DOWN:
                snake[0].changeSpeed(0, 25)
            elif event.key == pygame.K_LEFT:
                snake[0].changeSpeed(-25, 0)
            elif event.key == pygame.K_RIGHT:
                snake[0].changeSpeed(25, 0)




    feld.fill(BG)
    snake[0].update()
    allKaestchen.draw(feld)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
