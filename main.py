import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play=Player()
car=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(play.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    #Detect Collision With Cars

    for cars in car.all_cars:
        if cars.distance(play) < 20:
            game_is_on=False
            score.game_over()

    #Detect Successful Crossing

    if play.ycor()>280:
        game_is_on=False
        play.restart()
        car.level_up()
        score.increase_level()
        game_is_on=True

screen.exitonclick()
