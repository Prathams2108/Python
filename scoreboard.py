from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.increase_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT, )
