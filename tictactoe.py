"TicTacToe Game by Oliinyk Maksym"
import sys

icon_dict = []
PLAYER_ONE = "X"
PLAYER_TWO = "0"

for i in range(9):
    icon_dict.append(' ')


def print_board(icon_dict):
    """Game Board Creation"""
    # First Board.
    board = f"""
   {icon_dict[0]} | {icon_dict[1]} | {icon_dict[2]}
  ---|---|---
   {icon_dict[3]} | {icon_dict[4]} | {icon_dict[5]}
  ---|---|---
   {icon_dict[6]} | {icon_dict[7]} | {icon_dict[8]}

  """
    print(board)


index_list = []


def take_input(players_name):
    """"This function can take our inputs"""
    while True:
        x = int(input(f'{players_name}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print('This cell is occupied! Choose another one!')
                continue
            index_list.append(x)
            return x
        print('Coordinates should be from 1 to 9!')


def result_calculation(icon_dict, PLAYER_ONE, PLAYER_TWO):
    """This function will calculate our inputs"""
    if icon_dict[0] == icon_dict[1] == icon_dict[2] == 'X' or icon_dict[1] == icon_dict[4] == icon_dict[7] == 'X' or \
            icon_dict[0] == icon_dict[4] == icon_dict[8] == 'X' or icon_dict[2] == icon_dict[5] == icon_dict[
        8] == 'X' or icon_dict[3] == icon_dict[4] == icon_dict[5] == 'X' or icon_dict[2] == icon_dict[4] == icon_dict[
        6] == 'X' or icon_dict[6] == icon_dict[7] == icon_dict[8] == 'X' or icon_dict[0] == icon_dict[3] == icon_dict[
        6] == 'X':
        print(f'Congratulations {PLAYER_ONE}. You WON!')
        sys.exit('Thank you both for joining')
    elif icon_dict[0] == icon_dict[1] == icon_dict[2] == 'O' or icon_dict[1] == icon_dict[4] == icon_dict[7] == 'O' or \
            icon_dict[0] == icon_dict[4] == icon_dict[8] == 'O' or icon_dict[2] == icon_dict[5] == icon_dict[
        8] == 'O' or icon_dict[3] == icon_dict[4] == icon_dict[5] == 'O' or icon_dict[2] == icon_dict[4] == icon_dict[
        6] == 'O' or icon_dict[6] == icon_dict[7] == icon_dict[8] == 'O' or icon_dict[0] == icon_dict[3] == icon_dict[
        6] == 'O':
        print(f'Congratulations, {PLAYER_TWO}. You WON!')
        sys.exit('Thank you both for joining')
    else:
        return


def base():
    """Mine's project base"""
    print("Welcome to Oliinyk's TicTacToe Game" "\n Please Enter number between 1-9")
    print_board(icon_dict)
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(PLAYER_ONE)
            icon_dict[index] = 'X'
        else:
            index = take_input(PLAYER_TWO)
            icon_dict[index] = 'O'

        print_board(icon_dict)
        result_calculation(icon_dict, PLAYER_ONE, PLAYER_TWO)

    print("Draw. Play Again.")


base()
