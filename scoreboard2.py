from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,360)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def score_increase(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game Over\nFinal Score: {self.score}",align="center",font=("Arial",25,"normal"))
        


        
        
