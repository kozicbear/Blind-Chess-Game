class Game:

    BOARD_SIZE = (4, 3)

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

def main():
    from king import King
    game = Game()
    game.show_board()

    x_king = King([], 'X', (0, 1), [])
    x_legal_moves = x_king.get_legal_moves()

    o_king = King([], 'O', (3, 1), [])
    o_legal_moves = o_king.get_legal_moves()

    # this main class will have our two king objects
    # whenever we make a move
        # call update_king_pos with other king
        # so that that king knows where the other king/pieces is/are
        # this saves us space of having to store the entire board

if __name__ == "__main__":
    main()

