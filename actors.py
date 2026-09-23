"""The actors.py file contains the player and the enemy.
   This includes the movement, collision and all functions for the moving.
   game characters
"""

import turtle
from constants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_MOVE_SPEED

class Actor(turtle.Turtle):
    "General Actor blueprint"

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle() #to hide the turtle or draw
        self.penup() #this will give the turtle to not draw a line as it moves. That's why it set as empty parenthesis.
        self.speed(0) #this turns off the animation quickly

#for Pacman player
class Pacman(Actor):
    "Pac-man player"

    def __init__(self) -> None:
        super().__init__()
        self.showturtle()
        self.shape("circle")
        self.shapesize(1.4)
        self.pencolor("white")
        self.fillcolor("yellow")
        self.state = "stop" #this will stop pacman moving if the player decided to stop the character
        self.move_speed = PLAYER_MOVE_SPEED
        self.lives = 3 #this will show how many PACMAN live's he will get from the start of the game
        self.score = 0 #the default score will be zero at the first game


    #for the movement

    def move(self) -> None:
        if self.state != "stop":
            self.forward(self.move_speed)