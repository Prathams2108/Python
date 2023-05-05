import random;
import time
from turtle import Screen, Turtle
from Paddle import Paddle
from ball import ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("Black")
scr.title("PONG")
scr.tracer(0)

# Create the paddles and the ball for the game
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = ball()
score=Scoreboard()

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")

scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.bspeed)
    ball.move()
    scr.update()
    # Detect Collisions with the top wall or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collisions with r_paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect When r_Paddle misses the Ball

    if  ball.xcor() > 359 :
        ball.reset()
        r_paddle.goto(350,0)
        l_paddle.goto(-350,0)
        score.l_point()

    # Detect When l_Paddle misses the Ball

    if ball.xcor() < -359:
        ball.reset()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        score.r_point()

scr.exitonclick()
