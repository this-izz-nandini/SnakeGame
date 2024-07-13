from turtle import Turtle, Screen

START_POS=[(0,0),(-15,0),(-30,0)]
MOVE_DIST=15

class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment(i)
            
    def add_segment(self, position):
        t=Turtle(shape='square')
        t.shapesize(stretch_len=0.75,stretch_wid=0.75)
        t.color('white')
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def reset_snake(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            coor= self.segments[i-1].pos()
            self.segments[i].goto(coor)
        self.head.fd(MOVE_DIST)   

    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)
    def dwn(self): 
        if self.head.heading() !=90:
            self.head.setheading(270)
    def lft(self): 
        if self.head.heading() !=0:
            self.head.setheading(180)
    def rht(self): 
        if self.head.heading() !=180:
            self.head.setheading(0)