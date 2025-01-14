from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        # Stores heart objects in list
        self.player_lives = []

        # Create 3 heart shapes
        for x in range(3):
            life = Turtle()

            # draws the heart shapes
            life.speed(0)  # Fastest drawing speed (no animation)
            life.shape("turtle")
            life.color("red")
            life.penup()

            # Position hearts at the top of the screen
            life.goto(525 + (x * 23), 320)

            # Adjust the heart size to you liking here
            heart_size = 5

            # Draw the left half of the heart
            life.pendown()
            life.begin_fill()
            life.left(50)
            life.forward(heart_size * 2.5)
            life.circle(heart_size, 200)  #

            # Draw the right half of the heart
            life.right(140)
            life.circle(heart_size, 200)
            life.forward(heart_size * 2.5)

            # End the filling color & appends object to list
            life.end_fill()
            life.hideturtle()
            self.player_lives.append(life)

    def decrease_life(self):
        # Remove the last heart from the list
        life_to_remove = self.player_lives.pop()
        life_to_remove.clear()
