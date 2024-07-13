from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('powder blue')
        self.speed('fastest')
        self.reloc_food()
        
    def reloc_food(self):
        self.goto((random.randrange(-280,280),random.randrange(-280,280)))