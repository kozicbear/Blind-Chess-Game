class Board:
    x_king = (0, 1)
    o_king = (3, 1)
    board = []

    def __init__(self, row, col):
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
        self.board[piece.position[0]][piece.position[1]] = ' '
        self.board[move[0]][move[1]] = piece.letter