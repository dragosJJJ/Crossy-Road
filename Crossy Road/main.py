import random
import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

time_delay = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Crossy Road")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun= player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(time_delay)
    screen.update()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            screen.clear()
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= FINISH_LINE_Y:
        player.resett()
        scoreboard.level += 1
        scoreboard.update_level()
        time_delay -= 0.02

    car_manager.create_car()
    car_manager.move_cars()
    screen.update()




screen.exitonclick()