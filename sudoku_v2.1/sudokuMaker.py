#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sudoku game maker
http://code.activestate.com/recipes/578250-sudoku-game-generator/
https://github.com/Ripley6811/sudoku-py/commit/86782d09c777bfa2781af65b25f231c4e0adb57b

"""

__author__ = 'Ripley6811'
__contact__ = 'python at boun.cr'
__copyright__ = ''
__license__ = ''
__date__ = 'Thu Aug 30 10:09:06 2012'
__version__ = '0.1'

#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
from numpy import *

#===============================================================================
# METHODS
#===============================================================================


def new_block():
    return random.permutation(arange(1, 10)).reshape(3, 3)


def test_rowcol(s):
    retval = True
    for row in s:
        if len(set(row).difference([0])) < count_nonzero(row):
            retval = False
            break
    for col in s.T:
        if len(set(col).difference([0])) < count_nonzero(col):
            retval = False
            break
    return retval


def generate_grid(s=None):
    # PART 1: SET FIRST THREE ROWS AND FIRST THREE COLUMNS
    available = set(range(1, 10))
    if s is None:
        s = new_block()
        while True:
            srow = append(append(s, new_block(), 1), new_block(), 1)
            if test_rowcol(srow):
                break
        while True:
            scol = append(append(s, new_block(), 0), new_block(), 0)
            if test_rowcol(scol):
                scol = append(scol[3:], zeros((6, 6), int), 1)
                break
        s = append(srow, scol, 0)
    # PART 2: FILL IN THE REST OF GRID FROM PART 1. [3:, 3:]
    while True:
        s[3:6, 3:6] = new_block()
        if test_rowcol(s[:6, :6]):
            break
    while True:
        s[6:, 6:] = new_block()
        if test_rowcol(s):
            break
    for i in range(3, 9):
        for j in range(3, 9):
            if s[i, j] == 0:
                subset = available.difference(set(s[i])).difference(set(s[:, j]))
                if len(subset) == 1:
                    s[i, j] = subset.pop()
                else:
                    s[3:, 3:] = 0
                    return generate_grid(s)
    return s


def reduce_options(board, pcube):

    row, col = where(board == 0)
    playoption = []
    for i in range(9):
        for j in range(9):
            if board[i, j] != 0:
                pcube[i, j, pcube[i, j] != board[i, j]] *= 0

    for i, j in zip(row, col):
        exclude = set(board[i])
        exclude = exclude.union(board[:, j])
        exclude = exclude.union(board[i/3*3:i/3*3+3, j/3*3:j/3*3+3].flat)
        for each in exclude:
            pcube[i, j, pcube[i, j] == each] = 0

    for layer in pcube.T:  # probable layers 1 through 9
        for i in range(9):
            rowsfilled = sum(layer[i, :3]) > 0, sum(layer[i, 3:6]) > 0, sum(layer[i, 6:]) > 0
            if sum(rowsfilled) == 1:
                rowsfilled = repeat(rowsfilled, 3)
                layer[i/3*3+(i+1) % 3, rowsfilled] *= 0
                layer[i/3*3+(i+2) % 3, rowsfilled] *= 0
        layer = layer.T
        for i in range(9):
            rowsfilled = sum(layer[i, :3]) > 0, sum(layer[i, 3:6]) > 0, sum(layer[i, 6:]) > 0
            if sum(rowsfilled) == 1:
                rowsfilled = repeat(rowsfilled, 3)
                layer[i/3*3+(i+1) % 3, rowsfilled] *= 0
                layer[i/3*3+(i+2) % 3, rowsfilled] *= 0

    for i, j in zip(row, col):
        if count_nonzero(pcube[i, j]) == 1:
            playoption.append((i, j, sum(pcube[i, j])))
    return playoption


def generate_game(s):
    gametest = s.copy()

    for each in range(200):
        i = random.randint(81)
        temp = gametest.flat[i]
        gametest.flat[i] = 0

        if not isSolvable(gametest):
            gametest.flat[i] = temp
    return gametest


def isSolvable(testgame):
    board = testgame.copy()
    p = ones((9, 9, 9), int)
    for i in arange(9):
        p[:, :, i] *= i+1
    playorder = []
    laststate = sum(p)
    while sum(board == 0) > 0:
        # REDUCE OPTIONS FOR EACH HOLE
        playoptions = reduce_options(board, p)
        for i, j, v in playoptions:
            board[i, j] = v
        thisstate = sum(p)
        if thisstate == laststate:
            break
        else:
            laststate = thisstate
    return True if sum(board == 0) == 0 else False

