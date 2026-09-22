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

def calculate_maze_data(maze_level: list[str]) -> tuple[list, list, list]:
    "Setup maze level"
    walls: list = []
    pellets: list = []
    power_pellets: list = []

    #Iterate over each row of the maze level

    for row in range(MAZE_GRID_ROWS):
    # Iterate over each column of the maze level
        for column in range(MAZE_GRID_COLUMNS):
            # Store the coordinates of the character[row][column]
            character = maze_level[row][column]

            # row index starts from 0 to 36 (37 not included)
            character_x: float = MAZE_LEVEL_START_X + CELL_SIZE * column
            character_y: float = MAZE_LEVEL_START_Y + CELL_SIZE * row

            if character == "X":
                # append the coordinate of that wall to the walls list
                walls.append((character_x, character_y))
            elif character == ".":
                    pellets.append((character_x, character_y))
            elif character == "0":
                    power_pellets.append((character_x, character_y))
# Return the list with all the coordinates
#This allows us later to get this data in other files and store it as a variable

    return walls, pellets, power_pellets
        