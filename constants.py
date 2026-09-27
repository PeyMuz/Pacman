# Grid Size

import tkinter as tk


def _get_screen_resolution() -> tuple[int, int]:
    "Detect this machine's actual usable screen resolution"
    root = tk.Tk()
    root.withdraw()  # don't show this helper window, we just need the numbers
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height


# Original design size - the "ideal" cell size the game was built for
BASE_CELL_SIZE = 30

# Maze Size

MAZE_GRID_ROWS = 33
MAZE_GRID_COLUMNS = 28

# Detect the current screen so the maze always fits, whether we're on a
# big PC monitor or a smaller laptop display
_screen_width, _screen_height = _get_screen_resolution()

# Leave room for the window title bar / taskbar - don't use 100% of screen
_usable_width = _screen_width * 0.90
_usable_height = _screen_height * 0.85

# Biggest a cell can be while the WHOLE maze still fits on THIS screen
_max_cell_width = _usable_width / MAZE_GRID_COLUMNS
_max_cell_height = _usable_height / MAZE_GRID_ROWS

# Only shrink cells to fit a smaller screen - never grow past the
# original design size
CELL_SIZE = min(BASE_CELL_SIZE, _max_cell_width, _max_cell_height)

# How much smaller (1.0 = unchanged) everything drawn on the grid needs
# to scale to match CELL_SIZE - used by renderer.py and actors.py
SCALE_FACTOR = CELL_SIZE / BASE_CELL_SIZE

SCREEN_WIDTH = int(CELL_SIZE * MAZE_GRID_COLUMNS) + 40
SCREEN_HEIGHT = int(CELL_SIZE * MAZE_GRID_ROWS) + 100

GRID_ROWS = SCREEN_HEIGHT // CELL_SIZE
GRID_COLUMNS = SCREEN_WIDTH // CELL_SIZE

ROW_MARGIN = (SCREEN_WIDTH - (CELL_SIZE * GRID_COLUMNS)) / 2
COLUMN_MARGIN = (SCREEN_HEIGHT - (CELL_SIZE * GRID_ROWS)) / 2


# Maze starting position

ROW_MARGIN = (SCREEN_WIDTH - (CELL_SIZE * MAZE_GRID_COLUMNS)) / 2
COLUMN_MARGIN = (SCREEN_HEIGHT - (CELL_SIZE * MAZE_GRID_ROWS)) / 2

MAZE_LEVEL_START_X = (-SCREEN_WIDTH / 2) + ROW_MARGIN + (CELL_SIZE / 2)
MAZE_LEVEL_START_Y = (SCREEN_HEIGHT / 2) - COLUMN_MARGIN - (CELL_SIZE / 2)

#forthe movement of Pacman
PLAYER_MOVE_SPEED = 5 * SCALE_FACTOR