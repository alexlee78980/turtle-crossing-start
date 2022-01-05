import time
from turtle import Screen
import turtle_crossing.player as player
from turtle_crossing.player import Player
from turtle_crossing.car_manager import CarManager
from turtle_crossing.scoreboard import Scoreboard
import turtle_crossing.scoreboard as scoreboard


def turtle_crossing_start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    turtle = Player()
    cars = CarManager()
    score = Scoreboard()
    screen.listen()
    screen.onkey(turtle.move_forward, "Up")
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.generate()
        cars.move()
        if turtle.ycor() >= player.FINISH_LINE_Y:
            turtle.reset()
            scoreboard.LEVEL += 1
            score.reset()

        for car in cars.list_of_cars:
            if abs(turtle.xcor() - car.xcor()) < 18 and abs(turtle.ycor() - car.ycor()) < 10:
                score.game_over()
                game_is_on = False

    screen.exitonclick()
