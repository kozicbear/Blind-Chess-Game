import time
from king import King
from board import Board

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

o_tranistion_matrix = {
    "UPLEFT": 0.3,
    "UP": 0.1,
    "UPRIGHT": 0.1,
    "RIGHT": 0.1,
    "LEFT": 0.1,
    "DOWNLEFT": 0.1,
    "DOWN": 0.1,
    "DOWNRIGHT": 0.1
}

def convert_move(piece, string_move):
    y = piece.position[0]
    x = piece.position[1]
    
    if "UP" in string_move:
        y -= 1
    if "DOWN" in string_move:
        y += 1
    if "LEFT" in string_move:
        x -= 1
    if "RIGHT" in string_move:
        x += 1
    return (y, x)

def check_game_over(x_piece, o_piece):
    if x_piece.position == o_piece.position:
        return True

class Game:    

    def main():
        print("Welcome to the blind chess game\nInspired by Markhov Chains.\nTo begin please enter your desired board\n")
        row = int(input("Enter board row size: "))
        col = int(input("Enter board column size: "))
        game = Board(row, col)
        game.show_board()

        x_king = King(x_tranistion_matrix, 'X', (0, col // 2), (row, col))
        o_king = King(o_tranistion_matrix, 'O', (row - 1, col // 2), (row, col))

        game_over = False
        turn = 'X'

        while game_over == False:
            time.sleep(1)
            if turn == 'X':
                x_legal_moves = x_king.get_legal_moves()
                next_move = x_king.pick_move(x_legal_moves)
                # change that move from string to the new position piece will be at
                x_y_move = convert_move(x_king, next_move)

                game.make_move(x_king, x_y_move)
                x_king.update_position(x_y_move)
                turn = 'O'
                game.show_board()
                if check_game_over(x_king, o_king):
                    game_over = True
            else:
                o_legal_moves = o_king.get_legal_moves()
                next_move = o_king.pick_move(o_legal_moves)
                x_y_move = convert_move(o_king, next_move)
                game.make_move(o_king, x_y_move)
                o_king.update_position(x_y_move)
                turn = 'X'
                game.show_board()
                if check_game_over(x_king, o_king):
                    game_over = True

        if turn == 'X':
            print("O piece wins!\n")
        else:
            print("X piece wins!\n")

    if __name__ == "__main__":
        main()