"""
This code will create the maze.

X = wall.
. = Pellet
0 = Power Pellet

"""

from constants import (CELL_SIZE, MAZE_GRID_ROWS, MAZE_GRID_COLUMNS, MAZE_LEVEL_START_X, MAZE_LEVEL_START_Y)

maze_level_1: list[str] = [
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X 0 . . . . . . . . . . . X X . . . . . . . . . . . 0 X",
    "X . X X X X . X X X X X . X X . X X X X X . X X X X . X",
    "X . X X X X . X X X X X . X X . X X X X X . X X X X . X",
    "X . X X X X . X X X X X . X X . X X X X X . X X X X . X",
    "X . . . . . . . . . . . . . . . . . . . . . . . . . . X",
    "X . X X X X . X X . X X X X X X X X . X X . X X X X . X",
    "X . X X X X . X X . X X X X X X X X . X X . X X X X . X",
    "X 0 . . . . . X X . . . . X X . . . . X X . . . . . 0 X",
    "X X X X X X . X X X X X . X X . X X X X X . X X X X X X",
    "X X X X X X . X X X X X . X X . X X X X X . X X X X X X",
    "X X X X X X . X X . . . . . . . . . . X X . X X X X X X",
    "X X X X X X . X X . X X X = = X X X . X X . X X X X X X",
    "X X X X X X . X X . X             X . X X . X X X X X X",
    "0 . . . . . . . . . X             X . . . . . . . . . 0",
    "X X X X X X . X X . X             X . X X . X X X X X X",
    "X X X X X X . X X . X X X X X X X X . X X . X X X X X X",
    "X X X X X X . X X . . . . . . . . . . X X . X X X X X X",
    "X X X X X X . X X . X X X X X X X X . X X . X X X X X X",
    "X X X X X X . X X . X X X X X X X X . X X . X X X X X X",
    "X 0 . . . . . . . . . . . X X . . . . . . . . . . . 0 X",
    "X . X X X X . X X X X X . X X . X X X X X . X X X X . X",
    "X . X X X X . X X X X X . X X . X X X X X . X X X X . X",
    "X . . . X X . . . . . . . . . . . . . . . . X X . . . X",
    "X X X . X X . X X . X X X X X X X X . X X . X X . X X X",
    "X X X . X X . X X . X X X X X X X X . X X . X X . X X X",
    "X . . . . . . X X + . . . X X . . . . X X . . . . . . X",
    "X . X X X X X X X X X X . X X . X X X X X X X X X X . X",
    "X . X X X X X X X X X X . X X . X X X X X X X X X X . X",
    "X 0 . . . . . . . . . . . 0 . . . . . . . . . . . . 0 X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X"
]

def calculate_maze_data(maze_level: list[str]) -> tuple[list, list, list]:

    "Setup maze level"

    walls: list = []
    pellets: list = []
    power_pellets: list = []

    # Each row needs 55 characters:
    # 28 cells = 28 characters + 27 spaces
    row_length = (MAZE_GRID_COLUMNS * 2) - 1

    # Iterate over each row
    for row in range(MAZE_GRID_ROWS):

        # Make sure every row has the required length
        maze_row = maze_level[row].ljust(row_length)

        # Iterate over each column
        for column in range(MAZE_GRID_COLUMNS):

            # Get the character of the current cell
            character = maze_row[column * 2]

            # Calculate coordinates
            character_x: float = MAZE_LEVEL_START_X + CELL_SIZE * column
            character_y: float = MAZE_LEVEL_START_Y - CELL_SIZE * row

            if character == "X":

                walls.append((character_x, character_y))

            elif character == ".":

                pellets.append((character_x, character_y))

            elif character == "0":

                power_pellets.append((character_x, character_y))

    return walls, pellets, power_pellets