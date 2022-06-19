from random import randint

WIDTH = 5
HEIGHT = 5


def rand_num():
    cell_state = randint(0, 1)
    return cell_state


def random_state():
   board = [[rand_num() for i in range(HEIGHT)] for j in range(WIDTH)]
   return board


def replace_cell_state_symbol():
    board = random_state()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board[i][j] = " "
            else:
                board[i][j] = u"\u2588"
    return board


def next_board_state(initial_state):
    initial_state

    return next_board_state


def render_board_state():
    board = replace_cell_state_symbol()
    for i in range(len(board)):
        board_str = " ".join(board[i])
        print(board_str + "\n")


if __name__ == "__main__":
    render_board_state()    