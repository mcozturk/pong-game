from turtle import Turtle, Screen
from scoreboard import Scoreboard
from platform import Platform
from ball import Ball


def platform_touch():
    if platform.right_platform.distance(ball) < 50 and ball.xcor() > 350 or \
            platform.left_platform.distance(ball) < 50 and ball.xcor() < -350:
        ball.setheading(180 - ball.heading())


screen = Screen()
turtle = Turtle()
platform = Platform()
ball = Ball()
screen.setup(800, 600)
screen.bgcolor("black")
scoreboard = Scoreboard()
screen.tracer(0)
ball.start()
should_continue = True
while should_continue:
    platform_touch()
    if ball.xcor() > 360:
        scoreboard.add_score("left")
        ball.refresh()
        platform.refresh()

    elif ball.xcor() < -360:
        scoreboard.add_score("right")
        ball.refresh()
        platform.refresh()
    ball.move()
    ball.walls()
    screen.onkeypress(fun=platform.left_up, key="w")
    screen.onkeypress(fun=platform.left_down, key="s")
    screen.onkeypress(fun=platform.right_up, key="Up")
    screen.onkeypress(fun=platform.right_down, key="Down")
    screen.listen()
    screen.update()
screen.exitonclick()
