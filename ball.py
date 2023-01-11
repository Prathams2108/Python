from turtle import Turtle


class ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.bspeed = 0.1
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.speed(5)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.bspeed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1
        new_x= self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.bspeed=0.1
        self.speed(5)
        self.goto(new_x, new_y)
