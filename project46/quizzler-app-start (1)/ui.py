THEME_COLOR = "#375362"

import tkinter as tk
from quiz_brain import QuizBrain

class QuizInterface(tk.Tk):


    def __init__(self,quiz_brain:QuizBrain):
        super().__init__()

        self.quiz=quiz_brain
        
        self.title("QuizBrain")
        self.configure(bg="gray")
        self.geometry("500x600")

        label=tk.Label(self,text="Score:0",font=("Arial",12),bg="gray",fg="white")
        label.place(x=390,y=20)
        self.img=tk.PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project46/quizzler-app-start (1)/images/false.png")

        def on_button_click_false():
            is_right=self.quiz.check_answer("False")
            self.give_feedback(is_right)

        button=tk.Button(self,image=self.img,command=on_button_click_false,highlightthickness=0)
        button.place(x=100,y=400)



        self.img2=tk.PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project46/quizzler-app-start (1)/images/true.png")

        def on_button_click_true():
            is_right=self.quiz.check_answer("True")
            self.give_feedback(is_right)


        button=tk.Button(self,image=self.img2,command=on_button_click_true,highlightthickness=0)
        button.place(x=300,y=400)


        self.canvas=tk.Canvas(self,width=400,height=300,bg="White")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            fill="black",
            font=("Arial",12,"italic"),
            )
        
        self.canvas.place(x=50,y=80)

       



        




        self.get_next_question()

       




        self.mainloop()



    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
        
        

    
    def give_feedback(self,is_right):
            if is_right:
                 print("right")
            else:
                 print("false")
                
           
                
           
        

    

