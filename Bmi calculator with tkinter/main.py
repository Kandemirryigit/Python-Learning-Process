from tkinter import *  # From tkinter import everything

window=Tk() # To define tkinter
window.title("Bmi Calculator")  # To determine window's title
window.minsize(600,400)  # To determine window's size
window.config(bg="beige")  # To determine window's backgroundcolor

title=Label(text="Bmi Calculator",font=("Arial",20,"bold"),fg="#A94A4A",bg="beige")  # To create text
title.place(x=200,y=10)  # To determine text's location

var1=Label(text="Bmi≤18.4 | Underweight",font=("Arial",10),fg="#889E73",bg="beige")
var1.place(x=10,y=10)

var2=Label(text="18.5<Bmi≤24.9 | Normal",font=("Arial",10),fg="#889E73",bg="beige")
var2.place(x=10,y=40)

var3=Label(text="25≤Bmi≤39.9 | Overweight",font=("Arial",10),fg="#889E73",bg="beige")
var3.place(x=10,y=70)

var4=Label(text="Bmi≥40 | Obese",font=("Arial",10),fg="#889E73",bg="beige")
var4.place(x=10,y=100)

weight_text=Label(text="Weight:",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
weight_text.place(x=150,y=162)

height_text=Label(text="Height:",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
height_text.place(x=150,y=200)

result_text=Label(text="Result:",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
result_text.place(x=150,y=240)

after_config=Label(text="-",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
after_config.place(x=260,y=240)

kg_text=Label(text="Kg",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
kg_text.place(x=380,y=162)

m_text=Label(text="m",font=("Arial",12,"bold"),fg="#A94A4A",bg="beige")
m_text.place(x=380,y=198)

weight_entry=Entry()  # To create input
weight_entry.focus()  # To create blinking cursor
weight_entry.place(x=250,y=165)  # To determine input's location

height_entry=Entry()
height_entry.place(x=250,y=200)



def calculate():
    bmi=float(weight_entry.get())/(float(height_entry.get())**2)  # bmi formula
    if bmi<=18.4:
        after_config.config(text=f"Underweight ({bmi:.1f})")  # :.1f means just show 1 chracter after point in float numbers
    elif 18.5<bmi<=24.9:
        after_config.config(text=f"Normal ({bmi:.1f})")
    elif 25<=bmi<=39.9:
        after_config.config(text=f"Overweight ({bmi:.1f})")
    elif bmi>=40:
        after_config.config(text=f"Obese ({bmi:.1f})")


calculate_button=Button(text="Calculate",command=calculate,width=30,height=1)  # To create button
calculate_button.place(x=180,y=280)  # To determine button's location


window.mainloop()  # If I don't click exit button the screen is not gonna close