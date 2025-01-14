from turtle import Turtle, Screen
from blocks import Blocks
from paddle import Paddle
from ball import Ball
from soundeffects import Sound_effects
from lives import Lives
import time

# Constants
START_POSITION_CENTER = (0, -335)
PLAYING_GAME = True


def restart_game():
    global my_paddle, ball, blocks, lives, PLAYING_GAME

    # resets the game screen, paddle, ball, and block location
    turtle.hideturtle()
    turtle.clear()
    blocks = Blocks()
    lives = Lives()
    my_paddle.goto(START_POSITION_CENTER)
    ball.reset(x=my_paddle.xcor(), y=my_paddle.ycor()+22)
    sound_effect.switch_music_on()
    screen.update()

    # set constant to true & calls play game function
    PLAYING_GAME = True
    play_game()


def exit_game():
    quit()


#  initialized classes for ball, screen, paddle, sound effects
turtle = Turtle()
screen = Screen()
paddle = Turtle()
ball = Ball()
sound_effect = Sound_effects()

# UI setup
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

# create paddle
my_paddle = Paddle(START_POSITION_CENTER)

# screen listens for key presses & executes functions
screen.listen()
screen.onkey(my_paddle.move_paddle_left, key="a")
screen.onkey(my_paddle.move_paddle_right, key="d")
screen.onkey(restart_game, key="Return")
screen.onkey(exit_game, key="Escape")

# create blocks and lives of player
blocks = Blocks()
lives = Lives()

# play's music
sound_effect.switch_music_on()


def play_game():
    global PLAYING_GAME

    while PLAYING_GAME:

        # sleeps screen for 0.05 seconds & updates screen inorder to move the ball
        time.sleep(ball.speed)
        screen.update()
        ball.move()

        # detect collision with right-side and right-side wall and bounce
        if ball.xcor() > 580 or ball.xcor() < -590:
            sound_effect.wall_bounce_sound_effect()
            ball.bounce_x()

        # detect collision with top-side wall and bounce
        if ball.ycor() > 340:
            sound_effect.wall_bounce_sound_effect()
            ball.bounce_y()

        # paddle miss / detect passing bottom-wall
        if ball.ycor() < -350:
            sound_effect.reset_bleep_sound_effect()
            lives.decrease_life()
            ball.reset(x=my_paddle.xcor(), y=my_paddle.ycor()+22)

        # detect collision with paddle
        if 80 >= my_paddle.xcor() - ball.xcor() >= -115 and ball.ycor() < -315:
            sound_effect.paddle_bounce_sound_effect()
            ball.bounce_y()

        # checks for ball & brick collision in green blocks list
        for block in blocks.new_block_list_green:
            if ball.distance(block) < 28:

                # plays sound for block impact
                sound_effect.block_bounce_sound_effect()

                print(f"cor of ball:{ball.xcor(), ball.ycor()}")
                print("touched green brick")

                # hides(visually) block & deletes block from list, increases speed
                block.hideturtle()
                block.clear()
                ball.increase_speed()

                # Get block's coordinates and size
                block_x = block.xcor()
                block_y = block.ycor()

                # Define brick's width and height
                block_width = 42  # Based on the `stretch_len` of the block (shapesize)
                block_height = 20  # Approximate height from your brick setup

                # Checks if the ball hit the left/right side of the brick
                if ball.xcor() < block_x - block_width / 2 or ball.xcor() > block_x + block_width / 2:

                    # removes block from list  & Reverse horizontal direction of ball
                    blocks.new_block_list_green.remove(block)
                    ball.bounce_x()
                    break

                # Checks if the ball hit the top/bottom of the brick
                elif ball.ycor() < block_y - block_height / 2 or ball.ycor() > block_y + block_height / 2:

                    # removes block from list  & Reverse vertical direction of ball
                    ball.bounce_y()
                    blocks.new_block_list_green.remove(block)
                    break

        # checks for ball & brick collision in yellow blocks list and repeats above code
        for block in blocks.new_block_list_yellow:
            if ball.distance(block) < 28:

                sound_effect.block_bounce_sound_effect()
                block.hideturtle()
                block.clear()
                ball.increase_speed()

                block_x = block.xcor()
                block_y = block.ycor()
                block_width = 45
                block_height = 20

                # Check if the ball hit the left/right side of the brick
                if ball.xcor() < block_x - block_width / 2 or ball.xcor() > block_x + block_width / 2:
                    ball.bounce_x()
                    blocks.new_block_list_yellow.remove(block)
                    break

                # Check if the ball hit the top/bottom of the brick
                elif ball.ycor() < block_y - block_height / 2 or ball.ycor() > block_y + block_height / 2:
                    ball.bounce_y()  # Reverse vertical direction
                    blocks.new_block_list_yellow.remove(block)
                    break

        # checks for ball & brick collision in orange blocks list and repeats explanation for green list
        for block in blocks.new_block_list_orange:
            if ball.distance(block) < 28:

                sound_effect.block_bounce_sound_effect()
                block.hideturtle()
                block.clear()
                ball.increase_speed()

                block_x = block.xcor()
                block_y = block.ycor()
                block_width = 45
                block_height = 20

                # Check if the ball hit the left/right side of the brick
                if ball.xcor() < block_x - block_width / 2 or ball.xcor() > block_x + block_width / 2:
                    blocks.new_block_list_orange.remove(block)
                    ball.bounce_x()  # Reverse horizontal direction
                    break

                # Check if the ball hit the top/bottom of the brick
                elif ball.ycor() < block_y - block_height / 2 or ball.ycor() > block_y + block_height / 2:
                    ball.bounce_y()
                    blocks.new_block_list_orange.remove(block)
                    break

        # checks for ball & brick collision in red blocks list and repeats explanation for green list
        for block in blocks.new_block_list_red:
            if ball.distance(block) < 28:

                sound_effect.block_bounce_sound_effect()
                block.hideturtle()
                block.clear()
                ball.increase_speed()

                block_x = block.xcor()
                block_y = block.ycor()
                block_width = 45
                block_height = 20

                # Check if the ball hit the left/right side of the brick
                if ball.xcor() < block_x - block_width / 2 or ball.xcor() > block_x + block_width / 2:
                    blocks.new_block_list_red.remove(block)
                    ball.bounce_x()  # Reverse horizontal direction
                    break

                # Check if the ball hit the top/bottom of the brick
                elif ball.ycor() < block_y - block_height / 2 or ball.ycor() > block_y + block_height / 2:
                    ball.bounce_y()  # Reverse vertical direction
                    blocks.new_block_list_red.remove(block)
                    break

        # checks for player has won (all blocks cleared)
        if len(blocks.new_block_list_green) + len(blocks.new_block_list_green) + len(blocks.new_block_list_green) + len(blocks.new_block_list_green) == 0:

            # Player has no blocks left, end the game, stop music, play you win sound
            sound_effect.switch_music_off()
            time.sleep(1)
            sound_effect.game_over_won()

            # stops the while loop
            PLAYING_GAME = False

            # Hide and clear all blocks
            for block_list in [blocks.new_block_list_green, blocks.new_block_list_yellow, blocks.new_block_list_orange,
                               blocks.new_block_list_red]:
                for block in block_list:
                    block.hideturtle()  # Hide the block
                    block.clear()  # Clear the block's drawing

            # refreshes screen to display changes
            screen.update()

            # displays text GAME-OVER
            turtle.color("green")
            turtle.write("GAME OVER YOU WON!", align="center", font=("Arial", 35, "normal"))
            turtle.penup()
            turtle.goto(0, turtle.ycor() - 20)
            turtle.write("press Enter if you would like to restart the game or Esc to exit", align="center", font=("Arial", 12, "normal"))

        # checks for player has lost all lives
        if len(lives.player_lives) == 0:

            # Player has no lives left, end the game, stop music, play you loose sound
            sound_effect.switch_music_off()
            time.sleep(1)
            sound_effect.game_over()

            # stops the while loop
            PLAYING_GAME = False

            # Hide and clear all blocks
            for block_list in [blocks.new_block_list_green, blocks.new_block_list_yellow, blocks.new_block_list_orange,
                               blocks.new_block_list_red]:
                for block in block_list:
                    block.hideturtle()  # Hide the block
                    block.clear()  # Clear the block's drawing

            # refreshes screen to display changes
            screen.update()

            # displays text GAME-OVER
            turtle.color("RED")
            turtle.write("GAME OVER YOU LOST!", align="center", font=("Arial", 35, "bold"))
            turtle.penup()
            turtle.goto(0, turtle.ycor() - 20)
            turtle.write("press Enter if you would like to restart the game or Esc to exit", align="center", font=("Arial", 12, "normal"))


# calls the game function
play_game()
screen.exitonclick()
