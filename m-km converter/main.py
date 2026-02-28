from tkinter import *  # From tkinter import everything

window=Tk()  # To define tkinter
window.minsize(400,200)  # To determine window sizes
window.title("metre to kilometre converter")  # To determine window's title


title=Label(text="m-km converting machine",font=("Arial",12,"bold")) # To create a text
title.place(x=100,y=0)  # The text's location

metre=Entry()  # To create an input
metre.place(x=150,y=50)  # Input's location

metre_label=Label(text="Metre",font=("Arial",12,"bold"))
metre_label.place(x=280,y=50)

km_measure_label=Label(text="0",font=("Arial",12,"bold"))
km_measure_label.place(x=200,y=85)

km_label=Label(text="Km",font=("Arial",12,"bold"))
km_label.place(x=280,y=80)

is_equal_to=Label(text="is equal to",font=("Arial",12,"bold"))
is_equal_to.place(x=60,y=80)


def button_clicked():
    new_measure=float(metre.get())/1000
    km_measure_label.config(text=new_measure)  # To change label's text


button=Button(text="Calculate",command=button_clicked)  # To create a button and give that button a command
button.place(x=180,y=120)  


window.mainloop()  # The screen is going to be open if I don't click exit button
