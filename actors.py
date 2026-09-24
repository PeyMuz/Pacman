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
        #this will let pacman disappear from the side and reappear on the opposite side
            if round(self.xcor()) < - SCREEN_WIDTH / 2:  # if it goes left, it will appear at the right
                self.setx(SCREEN_WIDTH / 2)
            elif round(self.xcor()) > SCREEN_WIDTH / 2: # if it goes right, it will appear at the left
                self.setx(-SCREEN_WIDTH / 2)


    #for movement

    def turn_right(self) -> None:
        self.setheading(0) # the number indicate kung saan nakaharaap dapat si pacman
        self.state = "move"

    def turn_left(self) -> None:
        self.setheading(180)
        self.state = "move"

    def turn_up(self) -> None:
        self.setheading(90)
        self.state = "move"

    def turn_down(self) -> None:
        self.setheading(270)
        self.state = "move"