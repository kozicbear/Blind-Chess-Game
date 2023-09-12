import time
from king import King
from board import Board

class Game:

    def main():
        
        game = Board()
        game.show_board()

        x_tranistion_matrix = {
            "UPLEFT": 0.3,
            "UP": 0.1,
            "UPRIGHT": 0.1,
            "RIGHT": 0.1,
            "LEFT": 0.1,
            "DOWNLEFT": 0.1,
            "DOWN": 0.1,
            "DOWNRIGHT": 0.1
        }

        x_king = King(x_tranistion_matrix, 'X', (0, 1), [])
        x_legal_moves = x_king.get_legal_moves()

        o_king = King([], 'O', (3, 1), [])
        o_legal_moves = o_king.get_legal_moves()

        #TODO: at some point I will have to change this so that previous move is chosen by user
        game_over = False
        turn = 'X'

        while game_over == False:
            time.sleep(1)
            if turn == 'X':
                next_move = x_king.pick_move(x_legal_moves)
                game.make_move('X', next_move)
                turn = 'O'
                game.show_board()
            # 'O' turn
            else:
                break

        game.show_board()
        # this main class will have our two king objects
        # whenever we make a move
            # call update_king_pos with other king
            # so that that king knows where the other king/pieces is/are
            # this saves us space of having to store the entire board
            # finally update the previous move

    if __name__ == "__main__":
        main()

