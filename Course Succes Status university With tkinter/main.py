from tkinter import *  # From tkinter import everything

window=Tk()  # To define tkinter
window.title("Course Succes Status")  # To determine window's title
window.minsize(600,400)  # To determine window's size
window.config(bg="#E5E1DA")  # To determine window's background color

# bg means: background color , fg means: foreground color
title_text=Label(text="Course Succes Status",font=("Monospace",24,"bold"),bg="#E5E1DA",fg="#89A8B2") # To create a text 
title_text.place(x=125,y=10)  # To determine text's location

var=IntVar()  # To store Check_mark's state 1 or 0

check_mark=Checkbutton(text="If you took the third exam, mark it",bg="#E5E1DA",font=("Arial",10,"italic"),variable=var)  # To create checkmark button
check_mark.place(x=120,y=80)  # To determine checkmark button's location

first_note_text=Label(text="First Note:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
first_note_text.place(x=120,y=130)

second_note_text=Label(text="Second Note:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
second_note_text.place(x=85,y=180)

third_note_text=Label(text="Third Note:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
third_note_text.place(x=110,y=230)

status_text=Label(text="Status:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="#B3C8CF")
status_text.place(x=160,y=280)

after_config=Label(text="-",font=("Arial",18,"bold"),bg="#E5E1DA",fg="#B3C8CF")
after_config.place(x=280,y=280)


first_note_entry=Entry()  # To create an input
first_note_entry.focus()  # To create a blinking cursor
first_note_entry.place(x=270,y=140)  # To determine input's location

second_note_entry=Entry()
second_note_entry.place(x=270,y=190)

third_note_entry=Entry()
third_note_entry.place(x=270,y=240)


# First exam is %30 of the entire exam
# Second exam is %70 of the entire exam
# Third exam: If you are unsuccesful with first two exam and if you want to take third exam we don't calculate second exam and third exam means %70 of the entire exam 

def calculate():
    if var.get()==0:
        total_note=float(first_note_entry.get())*0.3 + float(second_note_entry.get())*0.7
        if total_note>=60:
            after_config.config(text=f"{total_note:.2f} (Succesful)")   # :.2f means just show 2 chracter after point in float numbers
        else:
            after_config.config(text=f"{total_note:.2f} (Unsuccesful)")
    else:
        total_note=float(first_note_entry.get())*0.3 + float(third_note_entry.get())*0.7
        if total_note>=60:
            after_config.config(text=f"{total_note:.2f} (Succesful)")
        else:
            after_config.config(text=f"{total_note:.2f} (Unsuccesful)")

        
# To create a button
calculate_button=Button(text="Calculate",width=30,height=1,bg="#E5E1DA",fg="black",font=("Monospace",12,"bold"),command=calculate)
calculate_button.place(x=150,y=340)  # To determine button's location


window.mainloop()  # If I don't click exit button the screen is not gonna close




























