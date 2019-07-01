!/usr/bin/env python
from random import randrange as random
import pygame, sys

config = {
            'cell_size':    20,
            'collums':      8,
            'rows':         16,
            'delay':        750,
            'maxfps':       60,
}

colours = [
(0, 0,  0),
(255,   0,  0),
(0, 150,    0),
(0, 0,  255),
(255,   120,    0),
(255,   255,    0),
(180,   0,  255),
(0, 220,    220),
]

tetris_shapes = [
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

def rotate_clockwise(shape):
        return[[shape[y][x]
                for y in xrange(len(shape))]
            for x in xrange(len(shape[0])-1, -1,-1)]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                    if cell and board[ cy + off_y][ cx + off_x]:
                        return True
                    except IndexError:
                        return True
            return False

def remove_row(board, row):
    del board[row]
    return [[0 for i in xrange(config['cols'])]] + board
