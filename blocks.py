from turtle import Turtle

START_POSITION_CENTER = (0, -320)
y_axis = 0
x_axis = -600
block_starting_positions = [(x_axis, y_axis)]


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        # creates all blocks and handles blockr elated functions
        # constants
        self.y_axis = 50
        self.x_axis = -630
        self.block_starting_positions = [(self.x_axis, self.y_axis)]
        self.number_of_blocks = 27

        # lists of each block color to store objects
        self.new_block_list_green = []
        self.new_block_list_yellow = []
        self.new_block_list_orange = []
        self.new_block_list_red = []

        # calls create blocks functions
        self.create_blocks("green")
        self.create_blocks("yellow")
        self.create_blocks("orange")
        self.create_blocks("red")

    def create_blocks(self, color):
        # if color = green, create block starting from edge of screen with gap 45 from one another and calls add-block
        if color == "green":
            for y in range(self.number_of_blocks):
                self.x_axis += 45
                for x in [(self.x_axis, self.y_axis)]:
                    self.add_block(x, color)
        elif color == "yellow":
            print("yes color yellow")
            self.x_axis = -645
            for y in range(self.number_of_blocks):
                self.x_axis += 45
                print(self.x_axis)
                for x in [(self.x_axis, self.y_axis + 25)]:
                    self.add_block(x, color)
        elif color == "orange":
            print("yes color orange")
            self.x_axis = -630
            for y in range(self.number_of_blocks):
                self.x_axis += 45
                print(self.x_axis)
                for x in [(self.x_axis, self.y_axis + 50)]:
                    self.add_block(x, color)
        elif color == "red":
            print("yes color red")
            self.x_axis = -648
            for y in range(self.number_of_blocks):
                self.x_axis += 45
                print(self.x_axis)
                for x in [(self.x_axis, self.y_axis + 75)]:
                    self.add_block(x, color)

    def add_block(self, x, color):
        # handles the actual creation of each block object, shapesize, color, length, and positions them accordingly
        # appends to relative object color list
        new_block = Turtle()
        new_block.penup()
        new_block.shape("square")
        new_block.shapesize(stretch_len=2)
        new_block.color(color)
        new_block.goto(x)
        if color == "green":
            self.new_block_list_green.append(new_block)
        elif color == "yellow":
            self.new_block_list_yellow.append(new_block)
        elif color == "orange":
            self.new_block_list_orange.append(new_block)
        else:
            self.new_block_list_red.append(new_block)
