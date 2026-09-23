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
        self.shapesize(1.2)
        self.pencolor("white")
        self.fillcolor("dodger blue") #to color the walls

    def draw(self) -> None:
        "Draw the wall on  screen"
        # walls is a list of tuples, each tuple contains the x, y coordinates of
        # wall center iterate over each wall coordinate indide the walls list

        for x, y in self.walls:
            self.goto(x, y)
            #stamp the wall and save the stamp id of the coordinate in a variable
            self.stamp()


#for pellet
class Pellet(Pen):
    "pellet (dot)"

    def __init__(self) -> None:
        super().__init__()
        self.shape(name= "circle")
        self.shapesize(0.35, 0.35)
        self.pencolor("white")
        self.fillcolor("gold") #to color the walls

    def draw(self) -> None:
        "Draw pellet on the screen"

        for x, y in self.pellets:
            self.goto(x, y)
            #stamp the pellet and save the stamp id of the coordinate in a variable
            self.stamp()

#Power Pellett
class PowerPellet(Pen):
    "Power up that Pacman always eat"

    def __init__(self) -> None:
        super().__init__()
        self.shape(name="circle")
        self.shapesize(0.8, 0.8)
        self.pencolor("white")
        self.fillcolor("chartreuse")

    def draw(self) -> None:
        "Draw the power pellet on the screen"
        for x, y in self.power_pellets:
            self.goto(x, y)
            self.stamp()