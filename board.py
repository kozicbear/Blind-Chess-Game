"""
Class representing a chess like board that differs in
that its size is variable
"""

class Board:
    board = []

    def __init__(self, row, col):
        """ Creates a board of size row, col with an 'X' piece in 
            the middle of the col on row 0 and 'O' piece in the middle
            of col on the final row

            Args:
                row (int): the number of the rows
                col (int): the number of columns
        """
        for i in range(row):
            self.board.append([])
            for j in range(col):
                if i == 0 and j == (col // 2):
                    self.board[i].append('X')
                elif i == row - 1 and j == (col // 2):
                    self.board[i].append('O')
                else:
                    self.board[i].append(' ')

    def show_board(self):
        """ Method to print out a string representation of the board
        """
        visual =  ""
        height = len(self.board)
        width = len(self.board[0])
        for row in range(height):
            for col in range(width):
                if(col != width - 1):
                    visual += "|" + self.board[row][col]
                else:
                    visual += "|"+ self.board[row][col] + "|"
            if(row != height - 1):
                visual += "\n"
        visual += "\n"
        print(visual)

    def make_move(self, piece, move):
        """ Method to update the board according to a move

            Args:
                piece (King): the King piece making the move
                move (tuple): tuple of x, y coordinates representing move to make
        """
        self.board[piece.position[0]][piece.position[1]] = ' '
        self.board[move[0]][move[1]] = piece.letter