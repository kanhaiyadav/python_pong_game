from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, color="white"):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 30)
