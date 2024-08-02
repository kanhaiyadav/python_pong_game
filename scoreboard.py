from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.pendown()
        self.hideturtle()
        self.pencolor("orange")

    def r_update_score(self, r_score):
        self.clear()
        self.write(arg=r_score, align="center", font=("Courier", 50, "normal"))

    def l_update_score(self, l_score):
        self.clear()
        self.write(arg=l_score, align="center", font=("Courier", 50, "normal"))