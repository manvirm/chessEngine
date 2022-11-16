"""
Responsible for storing all the information
about the current state of chess game.
Also responsible for determining valid moves
at current position. Also keep a move log
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFunctions = {
            'p': self.getPawnMoves,
            'R': self.getRookMoves,
            'N': self.getKnightMoves,
            'B': self.getBishopMoves,
            'Q': self.getQueenMoves,
            'K': self.getKingMoves
        }
        self.whiteToMove = True
        self.moveLog = []
    """
    Takes a move as its parameter and executes it (not for castling, pawn promotion, and en passant)
    """
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players

    """
    Undo the last move made
    """
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #switch turns back
    """
    Al moves considering checks
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    """
    All moves without considering checks
    """
    def getAllPossibleMoves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of cols in given row
                turn = self.board[r][c][0]
                if((turn  == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove)):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves) #calls appropriate move function based on piece type
        return moves
    """
    Get all the piece moves for the specific piece located at row, col and add these moves to the list
    """
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove: #white pawn moves
            if self.board[r-1][c] == "--": #1 square pawn advance (if square infront is empty)
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--": #2 square pawn advance
                    moves.append(Move((r, c), (r-2, c), self.board))
            #capture to left
            if c-1 >= 0: #do not go off left side of board
                if self.board[r-1][c-1][0] == 'b': #enemy piece to capture
                    moves.append(Move((r, c), (r - 1, c-1), self.board))
            # capture to right
            if c+1 <= 7:  # do not go off right side of board
                if self.board[r - 1][c + 1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))
        else: #black pawn moves
            if self.board[r+1][c] == "--": #1 square pawn advance (if square infront is empty)
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--": #2 square pawn advance
                    moves.append(Move((r, c), (r+2, c), self.board))
            #capture to left
            if c-1 >= 0: #do not go off left side of board
                if self.board[r+1][c-1][0] == 'w': #enemy piece to capture
                    moves.append(Move((r, c), (r + 1, c-1), self.board))
            # capture to right
            if c+1 <= 7:  # do not go off right side of board
                if self.board[r + 1][c + 1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    def getRookMoves(self, r, c, moves):
        pass


    def getKnightMoves(self, r, c, moves):
        pass


    def getBishopMoves(self, r, c, moves):
        pass


    def getQueenMoves(self, r, c, moves):
        pass

    def getKingMoves(self, r, c, moves):
        pass

class Move():

    # Maps keys to values
    # key:value

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4" : 4,
                   "5": 3, "6": 2, "7": 1, "8":0}

    rowsToRanks = {v: k for k, v in ranksToRows.items()} #reverse dict

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    """
    Overriding the equals method ( the == checks if objects are same)
    """
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)



    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]








