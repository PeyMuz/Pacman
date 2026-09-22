import turtle

def init_screen():
    """Initialize main screen, and it returns when called"""

    # Create the game screen and store it in a variable
    screen = turtle.Screen()

    # Disable auto update
    screen.tracer(0)

    # Set screen title
    screen.title("PACMAN by Kylle Bantog")

    # Set screen size
    screen.setup(width=1000, height=600)

    #color of the background
    screen.bgcolor("black")

    return screen


#this function is a gam engine and runs in real time
def game_loop(screen) -> None:

  #update Screen
  screen.update()

def main() -> None:
   #this function starts a game, it setes everything up - the screen, the players levels.

   #Call the initialize function
   screen = init_screen()

   #Starts the game loop
   game_loop(screen)

   #keeps the main screen open
   screen.mainloop()



#this condition make sure the game is only starts when we run this file directly-
#not if it's being imported as a module in another file.
if __name__ == "__main__":
   main()