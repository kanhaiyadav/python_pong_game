from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ballspeed = 0.02

    def starting_direction(self, x):
        if x:
            self.setheading(180 - randint(-70, 70))
        else:
            self.setheading(randint(-70, 70))


