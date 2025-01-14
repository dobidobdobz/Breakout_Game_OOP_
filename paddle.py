from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # creates paddle
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=8)
        self.penup()
        self.goto(position)

    # handles movement of paddle to the right
    def move_paddle_right(self):
        self.goto(self.xcor() + 100, self.ycor())

    # handles movement of paddle to the left
    def move_paddle_left(self):
        self.goto(self.xcor() - 100, self.ycor())

