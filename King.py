class King:
    #TODO: ask if I could access this global directly from Game.py
    BOARD_SIZE = (4, 3)

    letter = ""
    position = ()
    pieces = [()]

    legal_moves = [[]]

    # game initializes two kings setting their letter
    # might simplify this by having it do this itself
    def __init__(self, transition_matrix, letter, position, pieces):
        self.transition_matrix = transition_matrix
        self.letter = letter
        # remember the way postion works is y,x
        self.position = (position[0], position[1])
        self.pieces = pieces

    def legal_moves(self):
        moves = []
        #find legal moves
        # if king at (0 , 1)  ---> | |K| |
        # check starting at (-1, 0) -- (-1, 1) .... all the way to (1, 2)
        left_up = (self.position[0] + 1, self.position[1] - 1)

        # from -1 to (4 - 1) ---> -1 to 2
        for y in range(left_up[0], left_up[0] + (self.BOARD_SIZE[0] - 1)):
            
            # from 0 to (3 - 1) ----> 0 to 2
            for x in range(left_up[1], left_up[1] + (self.BOARD_SIZE[1] - 1)):
                if y >= 0 and y < self.BOARD_SIZE[1]:
                    if x >= 0 and x < self.BOARD_SIZE[0]:
                        test_move = (y, x)
                        if test_move not in self.pieces:
                            moves.append(test_move)
        return moves

    def pick_move(self, legal_moves, markhov_chain):
        # from legal moves use the markov chain to pick the next move
        