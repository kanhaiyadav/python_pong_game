from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from obstacle import Obstacle
from random import randint


l_score = 0
r_score = 0
SPEED = 0.05
window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)


r_pad = Paddle(position=(350, 0), color="yellow")
l_pad = Paddle(position=(-350, 0), color="sky blue")
ball = Ball()
ball.starting_direction(1)
obstacle1 = Obstacle((0, 150))
obstacle2 = Obstacle((0, -150))
r_scoreboard = Scoreboard((100, 200))
l_scoreboard = Scoreboard((-100, 200))
l_scoreboard.l_update_score(l_score)
r_scoreboard.r_update_score(r_score)

window.listen()
window.onkeypress(key="Up", fun=r_pad.move_up)
window.onkeypress(key="Down", fun=r_pad.move_down)
window.onkeypress(key="w", fun=l_pad.move_up)
window.onkeypress(key="s", fun=l_pad.move_down)

state = True
while state:
    window.update()
    time.sleep(0.05)
    ball.forward(20)
    # detecting collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.setheading(-ball.heading())

    # detecting collision with obstacle
    elif ball.distance(obstacle1) < 30 or ball.distance(obstacle2) < 30:
        ball.setheading(randint(-360, 360))

    # detecting collision with right wall
    elif ball.xcor() > 330 and ball.distance(r_pad) < 50:
        # ball.ballspeed -= 0.0003
        if ball.distance(r_pad) > 45:
            ball.setheading(160 - ball.heading())
        else:
            ball.setheading(180 - ball.heading())

    # detecting collision with left wall
    elif ball.xcor() < -330 and ball.distance(l_pad) < 50:
        if ball.distance(l_pad) > 45:
            ball.setheading(160 - ball.heading())
        else:
            ball.setheading(180 - ball.heading())

    # detecting collision miss
    elif ball.xcor() > 400:
        ball.goto(0, 0)
        l_score += 1
        l_scoreboard.l_update_score(l_score)
        #ball.ballspeed = SPEED
        window.update()
        time.sleep(0.5)
        ball.starting_direction(1)
    elif ball.xcor() < -400:
        ball.goto(0, 0)
        r_score += 1
        #ball.ballspeed = SPEED
        r_scoreboard.r_update_score(r_score)
        window.update()
        time.sleep(0.5)
        ball.starting_direction(0)
    if r_score > 4:
        print("basu"
              " You won!")
        state = False
    elif l_score > 4:
        print("kanhaiya you won!")
        state = False
