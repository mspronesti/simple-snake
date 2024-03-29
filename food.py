from random import choice
from config import *


class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(FOOD_START)

    def reposition(self):
        self.setx(choice(range(- BORD, BORD, STEP)))
        self.sety(choice(range(- BORD, BORD, STEP)))
