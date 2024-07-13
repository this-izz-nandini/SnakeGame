from turtle import Turtle
ALIGNMENT='center'
FONT=('Courier',20,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open("data.txt") as f:
            self.high_score=int(f.read())
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)

    def reset_score(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score=0
        self.update_score()

    # REPLACED BY RESET SCORE
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT,font=FONT)
        
    def inc_score(self):
        self.score+=1
        self.update_score()