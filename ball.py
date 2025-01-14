from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # handles all functionality related to ball
        # creates ball, customizes it, sets speed and movement
        self.shape("circle")
        self.color("grey")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.goto(0, -305)
        self.x_move = 5
        self.y_move = 5
        self.speed = 0.03

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    # reverse's horizontal direction
    def bounce_x(self):
        self.x_move *= -1

    # reverse's vertical direction
    def bounce_y(self):
        self.y_move *= -1

    # reset ball position with x,y coordinates
    def reset(self, x, y):
        self.goto(x=x, y=y)
        self.bounce_y()
        self.bounce_x()
        self.speed = 0.04

    # increase's speed
    def increase_speed(self):
        self.speed *= 0.9
