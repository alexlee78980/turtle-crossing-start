from turtle import Turtle
import random
import turtle_crossing.scoreboard as scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.list_of_cars = []

    def generate(self):
        if random.randint(0, 2) == 1:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.setpos(300, random.randint(-300, 300))
            turtle.setheading(180)
            turtle.color(random.choice(COLORS))
            self.list_of_cars.append(turtle)

    def move(self):
        for turtle in self.list_of_cars:
            turtle.forward(5 + 10 * scoreboard.LEVEL - 1)