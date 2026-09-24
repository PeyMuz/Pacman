import turtle
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from renderer import Wall, Pellet, PowerPellet
from actors import Pacman

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

   #Call the initialize function
   screen = init_screen()

   wall_pen = Wall()
   pellet_pen = Pellet()
   power_pen = PowerPellet()

   #call the instance function
   wall_pen.draw()
   pellet_pen.draw()
   power_pen.draw()

   #Player starting position 

   player_start_coor = random.choice(pellet_pen.pellets)
   player_start_x = player_start_coor[0]
   player_start_y = player_start_coor[1]

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