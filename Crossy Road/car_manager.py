from turtle import Turtle
import random,time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def remove_cars(self):
        for car in self.all_cars:
            car.clear()