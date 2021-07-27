from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_y = 10
        self.move_x = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def bounce_y(self):
        # what happens when ball hits top or bottom of screen
        self.move_y *= -1

    def bounce_x(self):
        # what happens when ball hits paddle
        self.move_x *= -1
        self.move_speed *= 0.5
