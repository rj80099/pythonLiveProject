from food import Food
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",12,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update Score in screen'''
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        '''Reset score and update high score'''
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("...GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        '''Increase score and update screen'''
        self.score+=1
        self.clear()
        self.update_scoreboard()

