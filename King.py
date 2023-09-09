class King:
    #TODO: ask if I could access this global directly from Game.py
    BOARD_SIZE = (4, 3)
    MOVE_RANGE = 2

    transition_matrix = []
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

    def get_legal_moves(self):
        moves = []
        left_up = (self.position[0] - 1, self.position[1] - 1)

        for y in range(left_up[0], left_up[0] + (self.MOVE_RANGE + 1)):
            for x in range(left_up[1], left_up[1] + (self.MOVE_RANGE + 1)):
                # print("y: ", y, " x: ", x)
                if y >= 0 and y < self.BOARD_SIZE[0]:
                    if x >= 0 and x < self.BOARD_SIZE[1]:
                        # Do not allow king to stay in same position
                        if (y , x) != self.position:
                            moves.append((y , x))
        return moves

    #def pick_move(self, legal_moves, markhov_chain):
        # from legal moves use the markov chain to pick the next move