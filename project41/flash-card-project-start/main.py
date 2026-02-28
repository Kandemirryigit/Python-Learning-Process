import pandas
from tkinter import *
import random
import math


BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/data/vocabulary_meanings.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")



def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["Word"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="Turkish",fill="white")
    canvas.itemconfig(card_word,text=current_card["Meaning"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/data/Words_to_learn.csv",index=False)
    next_card()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.config(bg=BACKGROUND_COLOR)


flip_timer=window.after(3000,func=flip_card)



canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_img=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/images/card_front.png")
card_back_img=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,110,text="",font=("Ariel",35,"italic"))
card_word=canvas.create_text(390,240,text="",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)




wrong_image=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)



right_image=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project41/flash-card-project-start/images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)






next_card()





























window.mainloop()