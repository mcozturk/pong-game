from turtle import Turtle


class Platform:
    def __init__(self):
        self.platforms = []
        self.create_platform()
        self.right_platform = self.platforms[0]
        self.left_platform = self.platforms[1]

    def create_platform(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.speed("fastest")
        turtle.tilt(90)
        turtle.shapesize(stretch_len=5, stretch_wid=1)
        turtle.goto(360, 0)
        self.platforms.append(turtle)
        turtle = Turtle("square")
        turtle.penup()
        turtle.speed("fastest")
        turtle.color("white")
        turtle.tilt(90)
        turtle.shapesize(stretch_len=5, stretch_wid=1)
        turtle.goto(-360, 0)
        self.platforms.append(turtle)

    def right_up(self):
        if not self.right_platform.ycor() > 240:
            self.right_platform.goto(self.right_platform.xcor(), self.right_platform.ycor() + 20)

    def left_up(self):
        if not self.left_platform.ycor() > 240:
            self.left_platform.goto(self.left_platform.xcor(), self.left_platform.ycor() + 20)

    def right_down(self):
        if not self.right_platform.ycor() <= -240:
            self.right_platform.goto(self.right_platform.xcor(), self.right_platform.ycor() - 20)

    def left_down(self):
        if not self.left_platform.ycor() <= -240:
            self.left_platform.goto(self.left_platform.xcor(), self.left_platform.ycor() - 20)

    def refresh(self):
        self.right_platform.clear()
        self.right_platform.goto(360, 0)
        self.left_platform.clear()
        self.left_platform.goto(-360, 0)
