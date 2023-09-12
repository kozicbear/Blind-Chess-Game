"""
Class representing our "blind" Kings

- Kings move like they do in chess, that is in any direction around them for a total of 8 possible moves
- They utilize a transition matrix to decide where they will move
- Kings are in charge of knowing where they can move as well

Dependencies: numpy
"""

import numpy as np

class King:
    MOVE_RANGE = 2

    row, col = (0, 0)
    transition_matrix = {}
    letter = ""
    position = ()
    legal_moves = [[]]


    def __init__(self, transition_matrix, letter, position, board_size):
        """ Simulates a blind king that relies on a first order Markov chain
            Args:
                transition_matrix (dict): transition probabilities
                letter (str): the letter identifier of the King
                position (tuple): the starting location of the piece
                board_size (tuple): the number of rows and cols of the board
        """
        self.transition_matrix = transition_matrix
        self.letter = letter
        # remember the way postion works is y,x
        self.position = (position[0], position[1])
        self.row = board_size[0]
        self.col = board_size[1]

    def get_legal_moves(self):
        moves = []
        left_up = (self.position[0] - 1, self.position[1] - 1)

        for y in range(left_up[0], left_up[0] + (self.MOVE_RANGE + 1)):
            for x in range(left_up[1], left_up[1] + (self.MOVE_RANGE + 1)):
                # print("y: ", y, " x: ", x)
                if y >= 0 and y < self.row:
                    if x >= 0 and x < self.col:
                        # Do not allow king to stay in same position
                        if (y, x) != self.position:
                            moves.append((y , x))
        return moves

    def pick_move(self, legal_moves):
        legal_moves = self.convert_moves(legal_moves)

        # create new transition matrix that only contains legal moves
        legal_moves_matrix = {}

        for transition in self.transition_matrix.keys():
            if transition in legal_moves:
                legal_moves_matrix[transition] = self.transition_matrix.get(transition)

        # now have to reevaluate probabilties since they might not add to 1
        total_inv = 1.0/sum(legal_moves_matrix.values())
        legal_moves_matrix = {k:v*total_inv for k,v in legal_moves_matrix.items()}

        move = np.random.choice(legal_moves, 1, legal_moves_matrix)
        # print("move picked: ", move[0])
        # print("move type: ", type(str(move[0])))
        return str(move[0])

    #TODO: will probably want to test this as well
    def convert_moves(self, moves):
        y = self.position[0]
        x = self.position[1]

        string_moves = []
        for move in moves:
            string_move = ""
            if move[0] > y:
                string_move += "DOWN"
            if move[0] < y:
                string_move += "UP"
            if move[1] < x:
                string_move += "LEFT"
            if move[1] > x:
                string_move += "RIGHT"
            string_moves.append(string_move)

        return string_moves
    
    def update_position(self, position):
        self.position = position