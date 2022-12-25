import time, random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


turtle = Player()
scoreboard = Scoreboard()
screen.onkey(turtle.up, "Up")

game_is_on = True
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        new_car = CarManager()
        cars.append(new_car)
        num_car = 0

    for car in cars:
        car.move(scoreboard.score + 1)
        if turtle.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() >= FINISH_LINE_Y:
        turtle.refresh()
        scoreboard.level()

screen.exitonclick()