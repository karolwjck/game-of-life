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
                board[i][j] = "*"
    return board


def render_board_state():
    board = replace_cell_state_symbol()
    top_row = []
    btm_row = []
    for i in range(WIDTH):
        top_row.append(" -")
        btm_row.append(" -")
    btm_row_str = "".join(btm_row)
    top_row_str = "".join(top_row)
    print(top_row_str)
    for i in range(len(board)):
        board_str = " ".join(board[i])
        print("| " + board_str + " | \n")
    print(btm_row_str)