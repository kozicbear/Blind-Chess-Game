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

    # def test_king_moves(self):
    #     from King import King
    #     x_king = King([], 'X', (0, 1), [])
    #     x_legal_moves = x_king.get_legal_moves()
    #     assert x_legal_moves == [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]

    #     o_king = King([], 'O', (3, 1), [])
    #     o_legal_moves = o_king.get_legal_moves()
    #     assert o_legal_moves == [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]

    #     o_king = King([], 'O', (1, 1), [])
    #     o_legal_moves = o_king.get_legal_moves()
    #     assert o_legal_moves == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

def main():
    from king import King
    game = Game()
    game.show_board()

    x_king = King([], 'X', (0, 1), [])
    x_legal_moves = x_king.get_legal_moves()

    o_king = King([], 'O', (3, 1), [])
    o_legal_moves = o_king.get_legal_moves()

    # test cases
    # should ask Harmon how to do this or search up at some point
    # game.test_king_moves()

    # this main class will have our two king objects
    # whenever we make a move
        # call update_king_pos with other king
        # so that that king knows where the other king/pieces is/are
        # this saves us space of having to store the entire board

if __name__ == "__main__":
    main()

