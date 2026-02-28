from turtle import Turtle

# Consts
STARTİNG_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DİSTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):  # When we run snake make these operations
        self.segments=[]  # To store segments
        self.create_snake() # Run create_snake function
        self.head=self.segments[0] 

    def create_snake(self):
        for position in STARTİNG_POSITIONS:
            new_segment=Turtle("square") # To determine turtle's shape
            new_segment.color("pink") # To determine turtle's color
            new_segment.penup()  # If don't wanna write something
            new_segment.goto(position) # Go this specific location
            self.segments.append(new_segment) # Append every single segment to segments 


    def add_segment(self,position):
        new_segment=Turtle("square") 
        new_segment.color("pink") 
        new_segment.penup()  
        new_segment.goto(position) 
        self.segments.append(new_segment) 



    # This is so important too
    def extend(self):
        # Add new segment to the tail
        self.add_segment(self.segments[-1].position())

    
    # This is the most important thing in the code
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DİSTANCE)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



    # To move the snake
    def up(self):
        if self.head.heading()!= DOWN: # snake can't go over itself
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:  # snake can't go over itself
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!= RIGHT:  # snake can't go over itself
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:  # snake can't go over itself
            self.head.setheading(RIGHT)

    

        

        
    
    
    

   