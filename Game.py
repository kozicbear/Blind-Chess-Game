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
    game = Game()
    game.show_board()


    # this main class will have our two king objects
    # whenever we make a move
        # call update_king_pos with other king
        # so that that king knows where the other king/pieces is/are
        # this saves us space of having to store the entire board

if __name__ == "__main__":
    main()