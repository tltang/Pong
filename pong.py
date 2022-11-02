import turtle as t

MOVE_DISTANCE = 10


class Pong:

    def __init__(self, x=350, y=0):
        self.pongs = []
        self.create_pong(x, y)
        self.head = self.pongs[0]

    def create_pong(self, xcor, ycor):
        new_pong = t.Turtle(shape="square")
        new_pong.shapesize(stretch_wid=5, stretch_len=1)
        new_pong.color("white")
        new_pong.penup()
        new_pong.speed("fastest")
        new_pong.goto(x=xcor, y=ycor)
        self.pongs.append(new_pong)

    def up(self):
        new_y = self.pongs[0].ycor() + 20
        new_x = self.pongs[0].xcor()
        self.pongs[0].goto(new_x, new_y)

    def down(self):
        new_y = self.pongs[0].ycor() - 20
        new_x = self.pongs[0].xcor()
        self.pongs[0].goto(new_x, new_y)
