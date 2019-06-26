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
hallo
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
