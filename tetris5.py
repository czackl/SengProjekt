
from random import randrange as random
import pygame, sys

config = {
            'cell_size':    20,
            'collums':      8,
            'rows':         16,
            'delay':        750,
            'maxfps':       60,
}

farben = [
(0, 0,  0),
(255,   0,  0),
(0, 150,    0),
(0, 0,  255),
(255,   120,    0),
(255,   255,    0),
(180,   0,  255),
(0, 220,    220),
]

tetris_steine = [
    [[1,1,1],
     [0,1,0]],

    [[0,2,2],
     [2,2,0]],

    [[3,3,0],
     [0,3,3]],

    [[4,0,0],
     [4,4,4]],

    [[0,0,5],
     [5,5,5]],

    [[6,6,6,6]],

    [[7,7],
     [7,7]]
]

def drehen(shape):
        return[[shape[y][x]
                for y in xrange(len(shape))]
            for x in xrange(len(shape[0])-1, -1,-1)]

def collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                    if cell and board[ cy + off_y][ cx + off_x]:
                        return True
                    except IndexError:
                        return True
            return False

def remove_zeile(board, row):
    del board[row]
    return [[0 for i in xrange(config['cols'])]] + board

def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1][cx+off_x] +=val
    retrun mat1

def neues_Spielfeld():
    board = [ [ 0 for x in xrange(config['cols'])]
                    for y in xrange(config['rows']) ]
    board += [[ 1 for x in xrange(config['cols'])]]
    return board

class TetrisApp(object):
            def_init_(self):
                pygame.init()
                pygame.key.set_repeat(250,25)
                self.width = config['cell_size']*config['cols']
                self.height = config['cell_size']*config['rows']

                self.screen = pygame.display.set_mode((self.width, self.height))
                pygame.event.set_blocked(pygame.MOUSEMOTION)


                self.init_game()

            def new_stone(self):
                self.stone = tetris_shapes[rand(len(tetris_shapes))]
                self.stone_x = int(config['cols'] / 2 - len(self.stone[0])/2)
                self.stone_y = 0

                if check_collision(self.board,
                                    self.stone,
                                    (self.stone_x, self.stone_y)):
                         self.gameover = True

            def init_game(self):
                self.board = new_board()
                self.new_stone()

            def zentrierung(self, msg):
                for i, line in enumerate(msg.splitlines()):
                    msg_image = pygame.font.Font(
                            pygame.font.get_default_font(), 12).render(
                                    line, False, (255,255,255), (0,0,0))

                    msgim_center_x, msgim_center_y = msg_image.get_size()
                    msgim_center_x //=2
                    msgim_center_y //=2

                    self.screen.blit(msg_image, (
                        self.width // 2-msgim_center_x
                        self.height // 2-msgim_center_y+i*22))

            def draw_matrix(self, matrix, offset):
                    off_x, off_y = offset
                    for y, row in enumerate(matrix):
                        for x, val in enumerate(row):
                            if val:
                                    pygame.draw.rect(
                                            self.screen,
                                            colors[val],
                                            pygame.Rect(
                                                    (off_x+x) *
                                                        config['cell_size'],
                                                    (off_y+y) *
                                                        config['cell_size'],
                                                    config['cell_size'],
                                                    config['cell_size']), 0)


            def move(self, delta_x):
