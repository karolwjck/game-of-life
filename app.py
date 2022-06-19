from random import randint
import time

ALIVE = 1
DEAD = 0


# TODO: Add Unit Testing
# TODO: Add Documentation
# TODO: Add GENERATION variable to loop for a given number of generations
# TODO: Add ability to load an initial state from a file
# TODO: Add Ability to update Game of Life rules
# TODO: Implement a terminal UI (curses for Linux)


def rand_num():
    cell_state = randint(0, 1)
    return cell_state


def board_state_width(board_state):
    return len(board_state)


def board_state_height(board_state):
    return len(board_state[0])


def dead_state(width, height):
    dead_board = [[DEAD for _ in range(height)] for _ in range(width)]
    return dead_board

def random_state(width, height):
   board = [[rand_num() for _ in range(height)] for _ in range(width)]
   return board


def next_board_state(initial_state):
    width = board_state_width(initial_state)
    height = board_state_height(initial_state)
    new_board_state = dead_state()

    for x in range(0, width):
        for y in range(0, height):
            new_board_state[x][y] = cell_status_update((x,y), initial_state)

    return new_board_state


def cell_status_update(cell_coords, board_state):
    width = board_state_width(board_state)
    height = board_state_height(board_state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_alive_neighbours = 0

    # Iterate around the current cells neighbours
    for x1 in range((x-1), (x+1)+1):
        # Check to see if you're not off the WIDTH edge of the board
        if x1 < 1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            # Check to see if you're not off the HEIGHT edge of the board
            if y1 < 0 or y1 >= height: continue
            # Don't count the current cell as a neighbour
            if x1 == x and y1 == y: continue

            if board_state[x1][y1]:
                n_alive_neighbours += 1

            if board_state[x][y] == ALIVE:
                if n_alive_neighbours <= 1:
                    return DEAD
                elif n_alive_neighbours <= 3:
                    return ALIVE
                else:
                    return DEAD
                
            else:
                if n_alive_neighbours == 3:
                    return ALIVE
                else:
                    return DEAD


def render_board_state(board_state):
    # u"\u2588" unicode for a filled-in square
    display_as = {DEAD: " ", ALIVE: u"\u2588"}

    display_lines = []
    for y in range(0, board_state_height(board_state)):
        display_line = ""
        for x in range(0, board_state_width(board_state)):
            display_line += display_as[board_state[x][y]] * 2
        display_lines.append(display_line)
        print("\n".join(display_lines))


def game_loop(initial_state):
    next_board_state = initial_state

    while True:
        render_board_state(next_board_state)
        time.sleep(0.03)


if __name__ == "__main__":
    initial_state = random_state(40,20)
    game_loop(initial_state)