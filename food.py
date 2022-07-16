from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.food_pos()

    def food_pos(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-260, 270)
        self.goto(rand_x, rand_y)