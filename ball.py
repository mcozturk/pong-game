from turtle import Turtle
from random import randint
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.color("white")
        self.penup()
        self.shape("circle")
        self.speed("slow")

    def set_random_angle(self):
        global random_int
        random_int = randint(-180, 180)

    def start(self):
        self.set_random_angle()
        while not 30 > abs(random_int) > -30:
            self.set_random_angle()
        self.setheading(random_int)
        self.forward(0)

    def move(self):
        self.forward(20)
        time.sleep(0.04)

    def walls(self):
        if self.ycor() >= 270:
            self.setheading(-self.heading())
        elif self.ycor() <= -270:
            self.setheading(-self.heading())

    def refresh(self):
        self.reset()
        self.create_ball()
        self.setposition(0, 0)
        self.start()
