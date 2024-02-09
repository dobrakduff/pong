from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()
        new_x = self.xcor()
        self.goto(new_x, new_y + 20)

    def go_down(self):
        new_y = self.ycor()
        new_x = self.xcor()
        self.goto(new_x, new_y - 20)