from turtle import Turtle


class Lines(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,350)
        self.setheading(270)
        for i in range(16):
            self.color("White")
            self.forward(20)
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(10)
        
        
            

        
            



            
