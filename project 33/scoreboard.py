from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_WORD =("Courier", 16, "normal")
WORD= "Level:"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.score=1
        self.penup()
        self.goto(-200,243)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score,align="center",font=FONT)

    def increase_level(self):
        self.score+=1
        self.update_scoreboard()

    

       
        
class WordLevel(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.write(WORD,align="center",font=FONT_WORD)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.write("Game Over",align="Center",font=("Courier", 24, "normal"))

    
    
    
        
    
