#!/usr/bin/python3
import pygame
import random

K = (0, 0, 0)
BG = (230, 255, 230)
SNAKE = pygame.image.load("schlange.png")
SNAKE = pygame.transform.scale(SNAKE, QUADRAT_S_L, QUADRAT_S_L)
APPLE = pygame.image.load("apfel.png")
APPLE = pygame.transform.scale(APPLE, QUADRAT_S_L, QUADRAT_S_L)

FELD_H = 600
FELD_B = 600
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


def main():
    pygame.init()
    feld = pygame.display.set_mode ([FELD_B, FELD_H])
    clock = pygame.time.Clock()
    snake = []
    allKaestchen = pygame.sprite.Group()

    kaestchen = Kaestchen(K, QUADRAT_S_L, QUADRAT_S_L)
    kaestchen.rect.x = random.randrange(int(FELD_B/25))*25
    kaestchen.rect.y = random.randrange(int(FELD_H/25))*25

    snake.append(kaestchen)
    allKaestchen.add(kaestchen)

    apfel = Kaestchen(APPLE, QUADRAT_S_L, QUADRAT_S_L)
    apfel.rect.x = random.randrange(int(FELD_B/25))*25
    apfel.rect.y = random.randrange(int(FELD_H/25))*25
    allKaestchen.add(apfel)

    stop = False

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake[0].change_y != 25:
                    snake[0].changeSpeed(0, -25)
                elif event.key == pygame.K_DOWN and snake[0].change_y != -25:
                    snake[0].changeSpeed(0, 25)
                elif event.key == pygame.K_LEFT and snake[0].change_x != 25:
                    snake[0].changeSpeed(-25, 0)
                elif event.key == pygame.K_RIGHT and snake[0].change_x !=-25:
                    snake[0].changeSpeed(25, 0)

    hit_Kaestchen = pygame.sprite.spritecollide(snake[0], snake, False)
    if hit_Kaestchen and len(hit_Kaestchen) > 1:
        for element in snake:
            if element != snake[0]:
                allKaestchen.remove(element)
                snake = snake[:1]


    hit_Kaestchen = pygame.sprite.spritecollide(snake[0], [apfel], False)
    newKaestchen = None

    if hit_Kaestchen:
        newKaestchen = Kaestchen(K, QUADRAT_S_L, QUADRAT_S_L)
        newKaestchen.rect.x = snake[-1].rect.x
        newKaestchen.rect.y = snake[-1].rect.y

        snake.append(newKaestchen)
        allKaestchen.add(newKaestchen)

        while True:
            apfel.rect.x = random.randrange(int(FELD_B/25))*25
            apfel.rect.y = random.randrange(int(FELD_H/25))*25
            hit_Kaestchen = pygame.sprite.spritecollide(apfel, snake, False)

            if not hit_Kaestchen:
                break

    for index in range(len(snake)-1, 0 -1):
        snake[index].rect.x = snake[index -1].rect.x
        snake[index].rect.y = snake[index -1].rect.y

    snake[0].update()

    feld.fill(BG)
    allKaestchen.draw(feld)

    pygame.display.flip()
    clock.tick(8)

    pygame.quit()
if __name__ == "__main__":
    main()
