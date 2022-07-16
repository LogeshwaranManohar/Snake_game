#Welcome to my snake world

from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.dir_chg = 0

    def create_snake(self):
        for pos in POS:
            self.add_seg(pos)

    def add_seg(self, pos):
        seg = Turtle(shape="square")
        seg.penup()
        seg.goto(pos)
        self.snake.append(seg)
        if len(self.snake) % 2 == 0:
            seg.color("blue")
        else:
            seg.color("red")

    def extend(self):
        self.add_seg(self.snake[-1].position())

    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[num - 1].xcor()
            new_y = self.snake[num - 1].ycor()
            self.snake[num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DIST)
        self.dir_chg = 0

    def up(self):
        head = self.snake[0].heading()
        if head == 0 and self.dir_chg < 1:
            self.snake[0].left(90)
            self.dir_chg += 1
        elif head == 180 and self.dir_chg < 1:
            self.snake[0].right(90)
            self.dir_chg += 1

    def down(self):
        head = self.snake[0].heading()
        if head == 0 and self.dir_chg < 1:
            self.snake[0].right(90)
            self.dir_chg += 1
        elif head == 180 and self.dir_chg < 1:
            self.snake[0].left(90)
            self.dir_chg += 1

    def left(self):
        head = self.snake[0].heading()
        if head == 270 and self.dir_chg < 1:
            self.snake[0].right(90)
            self.dir_chg += 1
        elif head == 90 and self.dir_chg < 1:
            self.snake[0].left(90)
            self.dir_chg += 1

    def right(self):
        head = self.snake[0].heading()
        if head == 270 and self.dir_chg < 1:
            self.snake[0].left(90)
            self.dir_chg += 1
        elif head == 90 and self.dir_chg < 1:
            self.snake[0].right(90)
            self.dir_chg += 1
