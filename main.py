import turtle


def init_screen():
    "Initialize main screen, and it returns when called"

    #Create the game screen and store it in a var screen
    screen = turtle.Screen()
    #Disable auto update
    screen.tracer(0)
    #set screen title
    screen.title("PACMAN by Kylle Bantog ")