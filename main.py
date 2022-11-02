# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import turtle
# from turtle import Turtle, Screen
import random
import turtle as t
import time
from pong import Pong
from ball import Ball
# from food import Food
from scoreboard import Scoreboard


my_screen = t.Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
# tracer 0 is put in so at the beginning we won't see the paddle go from center to right
my_screen.tracer(0)

my_pong  = Pong(350, 0)
my_pong2 = Pong(-350, 0)
my_ball = Ball()
# my_food = Food()
my_scoreboard = Scoreboard()
my_screen.listen()
my_screen.onkey(my_pong.up, "Up")
my_screen.onkey(my_pong.down, "Down")
my_screen.onkey(my_pong2.up, "w")
my_screen.onkey(my_pong2.down, "x")
# # my_screen.onkey(key="c", fun=move_home)

lContinue = True
iDirection = 0
i1 = 0

while lContinue:
    # because tracer is turned off, you won't see the paddle unless you set the screen to update
    my_screen.update()
    time.sleep(my_ball.move_speed)
    my_ball.balls[0].direction = iDirection
    my_ball.move_forward()

    if my_ball.balls[0].ycor() > 280 or my_ball.balls[0].ycor() < -280:
        my_ball.bounce()

    if my_pong.pongs[0].distance(my_ball.balls[0]) < 50 and my_ball.balls[0].xcor() > 320:
        my_ball.bounce2()

    if my_pong2.pongs[0].distance(my_ball.balls[0]) < 50 and my_ball.balls[0].xcor() < -320:
        my_ball.bounce2()

    if my_ball.balls[0].xcor() > 380:
        my_ball.reset_position()
        my_scoreboard.score1()
    elif my_ball.balls[0].xcor() < -340:
        my_ball.reset_position()
        my_scoreboard.score2()

#
#
#
#     i1 = 0
#     for snake in my_pong.pongs[1:]:
#         i1 += 1
#         if my_pong.head.distance(snake) < 5:
#             print("at segment:", i1)
#             lContinue = False
#             my_scoreboard.game_over(2)

my_screen.exitonclick()

# def move_backwards():
#     new_turtle.backward(5)
#
# def move_counterclock():
#     current_heading = new_turtle.heading() + 5
#     new_turtle.setheading(current_heading)
#
# def move_clock():
#     current_heading = new_turtle.heading() - 5
#     new_turtle.setheading(current_heading)
#
# def move_home():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()