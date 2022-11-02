from turtle import Turtle
import random

ALIGNMENT = "Center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write("Scores: " + str(self.l_score), move=False, align=ALIGNMENT, font=('Arial', 20, 'bold'))
        self.goto(200, 200)
        self.write("Scores: " + str(self.r_score), move=False, align=ALIGNMENT, font=('Arial', 20, 'bold'))

    def score1(self):
        self.l_score += 1
        self.update_score()

    def score2(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, reason):
        if reason == 1:
            display_text = "GAME OVER! Hit the wall."
        else:
            display_text = "GAME OVER! Hit the tail."
        self.color("red")
        self.home()
        self.write(display_text, move=False, align="center", font=('Arial', 12, 'bold'))
