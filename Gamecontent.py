# Importing PyGame and required libraries

import pygame
import time
import sys


# Creating Class for defining the piece
class piece():
    # Defining piece properties
    def __init__(self, _type, color, look):
        self.type = _type
        self.color = color
        self.killable = None
        self.look = look


def createBoard():
    return  [[' ' for i in range(8)] for j in range(8)]


def printBoard(board):
    for i in range(8):
        print(board[i])


if __name__ == '__main__':

    board = createBoard()
    printBoard(board)

    bp = piece('p', 'B', 'bpawn.png')
    br = piece('r', 'B', 'brook.png')
    bk = piece('k', 'B', 'bknight.png')
    bb = piece('b', 'B', 'bBis.png')

    wp = piece('p', 'W', 'wpawn.png')
    wr = piece('r', 'W', 'wrook.png')
    wk = piece('k', 'W', 'wknight.png')
    wb = piece('b', 'W', 'wBis.png')

    bK = piece('K', 'B', 'bKing.png')
    bk.killable = False
    bQ = piece('Q', 'B', 'bQueen.png')

    wK = piece('K', 'W', 'wKing.png')
    wk.killable = False
    wQ = piece('Q', 'W', 'wQueen.png')

    