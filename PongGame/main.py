from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

PLAYER_1 = (-350, 0)
PLAYER_2 = (350, 0)

Score = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_L = Paddle(PLAYER_1)
paddle_R = Paddle(PLAYER_2)
ball = Ball()

screen.listen()
screen.onkey(paddle_L.up, "w")
screen.onkey(paddle_L.down, "s")
screen.onkey(paddle_R.up, "Up")
screen.onkey(paddle_R.down, "Down")

gameOn = True

while gameOn:
    time.sleep(ball.spd)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if (
        ball.distance(paddle_R) < 30 and ball.xcor() > 320 
        or ball.distance(paddle_L) < 30 and ball.xcor() < -320
    ):
        ball.bounceX()
        

    if ball.xcor() > 380:
        ball.Reset_Position()
        Score.L_increase()
    
    if ball.xcor() < -380:
        ball.Reset_Position()
        Score.R_increase()
    




screen.exitonclick()