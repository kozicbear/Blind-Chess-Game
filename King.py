import numpy as np

class King:
    #TODO: ask if I could access this global directly from Game.py
    BOARD_SIZE = (4, 3)
    MOVE_RANGE = 2

    transition_matrix = {}
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

    def pick_move(self, legal_moves):
        legal_moves = self.convert_moves(legal_moves)
        print(legal_moves)
        # from legal moves use the markov chain to pick the next move
        # TODO: ask how this method works to pick one move, from a list with probabilities,
        # where the legal moves does not neccesarily contain all the options in the list of 
        # probabilities
        # return np.random.choice(legal_moves, )
        return "DOWN"

        # need a way to map up, down etc to the digit value of the move

    #TODO: will probably want to test this as well
    def convert_moves(self, moves):
        y = self.position[0]
        x = self.position[1]
        string_moves = []
        for move in moves:
            string_move = ""
            # For simplicities sake I have coded this so that moves are from one pieces perspective
            # or the users perspective of the board. i.e right is the same direction despite facing
            # different directions for the pieces
            if self.letter == 'X':
                if move[0] > y:
                    string_move += "DOWN"
                if move[0] < y:
                    string_move += "UP"
                if move[1] < x:
                    string_move += "LEFT"
                if move[1] > x:
                    string_move += "RIGHT"
            else:
                if move[0] > y:
                    string_move += "UP"
                if move[0] < y:
                    string_move += "DOWN"
                if move[1] < x:
                    string_move += "LEFT"
                if move[1] > x:
                    string_move += "RIGHT"
            string_moves.append(string_move)

        return string_moves