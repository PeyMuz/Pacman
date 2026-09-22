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
    "X . . . . . . X X + . . . X X . . . . X X . . . . . 0 X",
    "X . X X X X X X X X X X . X X . X X X X X X X X X X . X",
    "X . X X X X X X X X X X . X X . X X X X X X X X X X . X",
    "X 0 . . . . . . . . . . . 0 . . . . . . . . . . . . 0 X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X",
    "X X X X X X X X X X X X X X X X X X X X X X X X X X X X"
]