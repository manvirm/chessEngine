"""
Main driver file,
responsible for handling user input and
displaying current game state object
"""

import pygame as p
from Chess import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


"""
Initialize global dictionary of images
Will be called once in main
"""
def load_images():
    pieces = ["wQ", "wK", "wB", "wK", "wR", "wp", "bK", "bQ", "bB", "bK", "bR","bp"]

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))