import turtle as t

MOVE_DISTANCE = 10


class Ball:

    def __init__(self):
        self.balls = []
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        new_ball = t.Turtle(shape="circle")
        new_ball.color("white")
        new_ball.penup()
        new_ball.speed("fastest")
        self.balls.append(new_ball)

    def up(self):
        new_y = self.balls[0].ycor() + 20
        new_x = self.balls[0].xcor()
        self.balls[0].goto(new_x, new_y)

    def down(self):
        new_y = self.balls[0].ycor() - 20
        new_x = self.balls[0].xcor()
        self.balls[0].goto(new_x, new_y)

    def move_forward(self):
        new_x = self.balls[0].xcor() + self.x_move
        new_y = self.balls[0].ycor() + self.y_move
        self.balls[0].goto(new_x, new_y)
        # self.balls[0].forward(MOVE_DISTANCE)

    def bounce(self):
        self.move_speed *= 0.9
        self.y_move *= -1

    def bounce2(self):
        self.move_speed *= 0.9
        self.x_move *= -1
        self.y_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.balls[0].goto(0, 0)
        self.bounce2()
