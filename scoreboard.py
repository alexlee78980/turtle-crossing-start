from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.reset()


    def reset(self):
        self.clear()
        self.write(f"Level: {LEVEL}", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over", font=FONT)
