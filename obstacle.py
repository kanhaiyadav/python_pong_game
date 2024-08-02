from turtle import Turtle


class Obstacle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.goto(position)