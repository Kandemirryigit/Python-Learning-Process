from turtle import Turtle  
import random  # to use random module

# Class inheritance
class Food(Turtle):
     
    def __init__(self): # When we run food make this operations
        super().__init__()  

        self.shape("circle") #To determine turtle's shape
        self.penup()  # To not draw something
        self.shapesize(0.5,0.5) # to determine sizes
        self.color("pink")  # to determine color
        self.speed("fastest") # To determine speed
        self.refresh()  
        

    def refresh(self):
        random_x=random.randint(-280,280)  # Random x cor.
        random_y=random.randint(-280,260)  # Random y cor.
        self.goto(random_x,random_y)  # Go this specific cor.
