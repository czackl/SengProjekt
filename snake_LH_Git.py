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

class Quadrat(pygame.sprite.Kaestchen):
    def __init__(self,color, width, height):
        super().__init__()

        self.image = pygame.Surfave([width, heigth])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

        def changeSpeed(self, x, y):
            self.change_x = x
            self.change_y = y



pygame.init()
screen = pygame.display.set_mode ([FELD_B, FELD_H])
clock = pygame.time.Clock()

snake = []
allKaestchen = pygame.sprite.Group()

kaestchen = Kaestchen(K, KAESTCHEN_SIDE_LENGTH, KAESTCHEN_SIDE_LENGTH)
kaestchen.rect.x = random.randrange(int(FELD_B/25))*25
kaestchen.rect.y = random.randrange(int(FELD_H/25))*25
snake.append(kaestchen)


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    screen.fill(BG)
    pygame.display.flip()
    clock.tick(25)

pygame.QUIT()
