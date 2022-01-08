from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))


    def update_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def update_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()



        


    