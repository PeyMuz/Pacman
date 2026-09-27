import turtle
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from renderer import Wall, Pellet, PowerPellet
from actors import Pacman

def fix_windows_dpi_scaling():
    """Force true 1:1 pixel rendering on Windows.

    Without this, Windows display scaling (125%, 150%, etc. - common on
    laptops with high-res but small screens) causes tkinter/turtle to
    mis-map pixels, making the window render as if zoomed in/cropped.
    This has no effect on Mac/Linux or on PCs already at 100% scaling.
    """
    if sys.platform == "win32":
        import ctypes
        try:
            # Per-monitor DPI aware (most accurate)
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                # Fallback for older Windows versions
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass


def init_screen():
    """Initialize main screen, and it returns when called"""

    # Create the game screen and store it in a variable
    screen = turtle.Screen()

    # Disable auto update
    screen.tracer(0)

    # Set screen title
    screen.title("PACMAN by Kylle Bantog")

    # Set screen size
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    #color of the background
    screen.bgcolor("black")

    return screen

#for key movements of PACMAN

def bind_controls(screen, player):
   "Keyboard and mouse bindings"
   screen.listen()
   screen.onkeypress(player.turn_right, "Right")
   screen.onkeypress(player.turn_left, "Left")
   screen.onkeypress(player.turn_up, "Up")
   screen.onkeypress(player.turn_down, "Down")


#this function is a gam engine and runs in real time
def game_loop(screen, player) -> None:
  "Reak time updates"
  player.move()
  #update Screen
  screen.update()
  screen.ontimer(lambda: game_loop(screen,player), 1000 // 60)

def main() -> None:
   #this function starts a game, it setes everything up - the screen, the players levels.

   #Fix DPI scaling issue BEFORE creating the window (laptop vs PC bug)
   fix_windows_dpi_scaling()

   #Call the initialize function
   screen = init_screen()

   wall_pen = Wall()
   pellet_pen = Pellet()
   power_pen = PowerPellet()

   #call the instance function
   wall_pen.draw()
   pellet_pen.draw()
   power_pen.draw()

   #Player starting position - always the fixed "+" spot in the maze, not random

   player_start_x, player_start_y = wall_pen.pacman_start

   #Create Pacman
   player = Pacman()
   player.goto(player_start_x, player_start_y)
   bind_controls(screen, player) # so it listen to the key presses and so the player can tun
   
   #Starts the game loop - moving things
   game_loop(screen,player)

   #keeps the main screen open
   screen.mainloop()



#this condition make sure the game is only starts when we run this file directly-
#not if it's being imported as a module in another file.
if __name__ == "__main__":
   main()