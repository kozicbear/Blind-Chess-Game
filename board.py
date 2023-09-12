class Board:
    BOARD_SIZE = (4, 3)
    x_king = (0, 1)
    o_king = (3, 1)
    board = [[]]

    # starting with just a king for simplicity
    # could add pawns in later
    def __init__(self):
        self.board = [
            [" ", "X", " "],
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", "O", " "]
        ]

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
        print(visual)

    def make_move(self, piece, move):
        move = self.convert_move(piece, move)
        print("move y: ", move[0])
        print("move x: ", move[1])

        if piece == 'X':
            print("removing from: ", self.x_king[0], self.x_king[1])
            self.board[self.x_king[0]][self.x_king[1]] == ' '
            print("moving X to: ", move[0], move[1])
            self.board[move[0]][move[1]] == 'X'
            self.x_king == (move[0], move[1])
        else:
            self.board[self.o_king[0]][self.o_king[1]] == ' '
            self.board[move[0]][move[1]] == 'O'
            self.o_king == (move[0], move[1])

    def convert_move(self, piece, string_move):
        y = 0
        x = 0
        if piece == 'X':
            y = self.x_king[0]
            x = self.x_king[1]
        else:
            y = self.o_king[0]
            x = self.o_king[1]
        
        if "UP" in string_move:
            y -= 1

        if "DOWN" in string_move:
            y += 1

        if "LEFT" in string_move:
            x -= 1

        if "RIGHT" in string_move:
            y += 1

        return (y, x)

            