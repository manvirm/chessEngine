"""
Responsible for storing all the information
about the current state of chess game.
Also responsible for determining valid moves
at current position. Also keep a move log
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bK", "bQ", "bB", "bK", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wK", "wR"]
        ]
        self.whiteToMove = True
        self.movelog = []