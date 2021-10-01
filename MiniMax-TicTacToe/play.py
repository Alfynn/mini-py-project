import time
from humanPlayer import HumanPlayer
from AIPlayer import AIPlayer
from board import board


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':

    x_player, o_player = None, None

    while x_player != '1' or '2':
        x_ask = input("X Player will be: (1) AI or (2) Human: ")
        if x_ask == '1':
            x_player = AIPlayer('X')
            break
        elif x_ask == "2":
            x_player = HumanPlayer('X')
            break
        else:
            print("Enter a valid input")
            continue

    while o_player != '1' or '2':
        o_ask = input("O Player will be: (1) AI or (2) Human: ")
        if o_ask == '1':
            o_player = AIPlayer('O')
            break
        elif o_ask == "2":
            o_player = HumanPlayer('O')
            break
        else:
            print("Enter a valid input")
            continue

t = board()
play(t, x_player, o_player, print_game=True)
