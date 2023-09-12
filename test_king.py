"""
Testing class to test king internal methods
"""

import unittest
from king import King

class TestGetLegalMoves(unittest.TestCase):
    def test_king_moves(self):
        from king import King
        x_king = King([], 'X', (0, 1), (4, 3))
        x_legal_moves = x_king.get_legal_moves()
        self.assertEqual(x_legal_moves, [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)], 
                         'incorrect legal moves have been found')

        o_king = King([], 'O', (3, 1), (4, 3))
        o_legal_moves = o_king.get_legal_moves()
        self.assertEqual(o_legal_moves, [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)],
                         'incorrect legal moves have been found')

        o_king = King([], 'O', (1, 1), (4, 3))
        o_legal_moves = o_king.get_legal_moves()
        self.assertEqual(o_legal_moves, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
                         'incorrect legal moves have been found')

class TestConvertMoves(unittest.TestCase):
    def test_convert_moves(self):
        from king import King
        x_king = King([], 'X', (1, 1), (4, 3))
        string_moves = ['UPLEFT', 'UP', 'UPRIGHT', 'LEFT', 'RIGHT', 'DOWNLEFT', 'DOWN','DOWNRIGHT']
        x_y_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(x_king.convert_moves(x_y_moves), string_moves, 
                         'incorrect legal moves have been found')
        
        o_king = King([], 'O', (3, 2), (4, 3))
        string_moves = ['UPLEFT', 'UP', 'LEFT']
        x_y_moves = [(2, 1), (2, 2), (3, 1)]
        self.assertEqual(o_king.convert_moves(x_y_moves), string_moves, 
                         'incorrect legal moves have been found')