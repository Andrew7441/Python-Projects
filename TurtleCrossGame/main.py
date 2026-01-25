import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.Move_Fd, "Up")
screen.onkey(player.Move_Bd, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.Create_Car()
    car.Move_Cars()

    if player.ycor() > 280:
        player.ResetPosition()
        car.IncreaseSpeed()
        score.Increase_Score()
    
    for car_obj in car.cars:
        if player.distance(car_obj) < 20:
            game_is_on = False
            score.Game_Over()

screen.exitonclick()