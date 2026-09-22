#Renderer for pacman game

import turtle
from mazes import calculate_maze_data, maze_level_1


class Pen(turtle.Turtle):
    "General Pen"

    def __init__(self):
        super().__init__()                     #super dot init passes all the built-in setup from Turtle to Pen    
        self.hideturtle()
        self.penup()
        self.speed(0) # this will show how turtle speeds the drawing. If you set numbers (e.g 1), it will slowly animate it. But if yo uset it to  0, it will turn off the animation
        self.walls, self.pellets, self.power_pellets = calculate_maze_data(
            maze_level= maze_level_1
        )


class Wall(Pen):
    "Maze wall"

    def __init__(self) -> None:
        super().__init__()
        self.shape(name= "square")
