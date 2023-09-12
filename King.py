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
        self.position = (position[0], position[1])
        self.row = board_size[0]
        self.col = board_size[1]

    def get_legal_moves(self):
        """ Gets legal moves from the king's current position
            Return:
                moves (list): list of legal moves
        """
        moves = []
        left_up = (self.position[0] - 1, self.position[1] - 1)

        for y in range(left_up[0], left_up[0] + (self.MOVE_RANGE + 1)):
            for x in range(left_up[1], left_up[1] + (self.MOVE_RANGE + 1)):
                if y >= 0 and y < self.row:
                    if x >= 0 and x < self.col:
                        # Do not allow king to stay in same position
                        if (y, x) != self.position:
                            moves.append((y , x))
        return moves

    def pick_move(self, legal_moves):
        """ Picks a move utilizing a transition matrix on a set of legal moves
            Args: 
                legal_moves (list): A list of legal moves in x, y form
            Return:
                A valid move in string form
        """

        # convert the moves into string form to adhere to transition matrix form
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
        return str(move[0])

    def convert_moves(self, moves):
        """ Helper method to convert a list of x, y coordinates representing moves
            a piece can make into a corresponding string form for the piece

            Args:
                moves (list): list of moves in x, y  form
            Return:
                List of string form moves relative to pieces position
        """
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
        """Updates the pieces internal memory of its location
            Args:
                position (tuple): tuple of x, y coordinate value to set piece to
        """
        self.position = position