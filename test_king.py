import unittest
from king import King

class TestGetLegalMoves(unittest.TestCase):
    def test_king_moves(self):
        from king import King
        x_king = King([], 'X', (0, 1), [])
        x_legal_moves = x_king.get_legal_moves()
        self.assertEqual(x_legal_moves, [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)], 
                         'incorrect legal moves have been found')

        o_king = King([], 'O', (3, 1), [])
        o_legal_moves = o_king.get_legal_moves()
        self.assertEqual(o_legal_moves, [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)],
                         'incorrect legal moves have been found')

        o_king = King([], 'O', (1, 1), [])
        o_legal_moves = o_king.get_legal_moves()
        self.assertEqual(o_legal_moves, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
                         'incorrect legal moves have been found')
                         