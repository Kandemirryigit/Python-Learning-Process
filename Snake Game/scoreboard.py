from turtle import Turtle 

# consts
ALIGN="center"
FONT=("Monospace",18,"bold")


class Scoreboard(Turtle):

    def __init__(self): # When we run scoreboard make this operations
        super().__init__()
        self.score=0 
        with open("C:/Users/CASPER/Desktop/python_projects/Snake Game/data.txt") as data:
            self.high_score=int(data.read())
        self.color("white") # to determine scoreboard's color
        self.hideturtle()  # To hide cursor
        self.penup()  # to not draw something
        self.goto(0,270)  # To go this specific location
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}           High Score: {self.high_score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over",align=ALIGN,font=FONT)

    
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("C:/Users/CASPER/Desktop/python_projects/Snake Game/data.txt","w") as data:
                data.write(f"{self.high_score}") 
        self.score=0
        self.update_scoreboard()
       
        
    
    def increase_score(self):
        self.score+=1
        self.clear()  # Clear all previous things
        self.update_scoreboard()

    



