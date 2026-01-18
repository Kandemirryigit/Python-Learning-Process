from tkinter import *  # From tkinter import everything

window=Tk()  # To define tkinter
window.title("Course Succes Status")  # To determine window's title
window.minsize(600,400)  # To determine window's size
window.config(bg="#E5E1DA")  # To determine window's background color

# bg means: background color , fg means: foreground color
title_text=Label(text="Course Succes Status",font=("Monospace",24,"bold"),bg="#E5E1DA",fg="#89A8B2") # To create a text 
title_text.place(x=125,y=10)  # To determine text's location

first_note_text=Label(text="First Note:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
first_note_text.place(x=125,y=80)

second_note_text=Label(text="Second Note:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
second_note_text.place(x=90,y=130)

teachers_note1_text=Label(text="Teacher's note1:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
teachers_note1_text.place(x=55,y=180)

teachers_note2_text=Label(text="Teacher's note2:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="black")
teachers_note2_text.place(x=55,y=230)

status_text=Label(text="Status:",font=("Arial",18,"bold"),bg="#E5E1DA",fg="#B3C8CF")
status_text.place(x=165,y=280)

after_config=Label(text="-",font=("Arial",18,"bold"),bg="#E5E1DA",fg="#B3C8CF")
after_config.place(x=285,y=280)


first_note_entry=Entry()  # To create an input
first_note_entry.focus()  # To create a blinking cursor
first_note_entry.place(x=270,y=90)  # To determine input's location

second_note_entry=Entry()
second_note_entry.place(x=270,y=140)

teachers_note1_entry=Entry()
teachers_note1_entry.place(x=270,y=190)

teachers_note2_entry=Entry()
teachers_note2_entry.place(x=270,y=240)


def calculate():
    try:
        first = int(first_note_entry.get())
        second = int(second_note_entry.get())
        teacher1 = int(teachers_note1_entry.get())
        teacher2 = int(teachers_note2_entry.get())
        exam_average=(first+second)/2
        average = (exam_average * 2 + teacher1 + teacher2) / 4  
        if average>=50:
            after_config.config(text=f"{average:.2f} (Successful)")
        else:
            after_config.config(text=f"{average:.2f} (Unsuccessful)")

    except ValueError:
        after_config.config(text=f"Invalid Input")   # If user don't type number.Because notes gotta be number 


# To create a button
calculate_button=Button(text="Calculate",width=30,height=1,bg="#E5E1DA",fg="black",font=("Monospace",12,"bold"),command=calculate)
calculate_button.place(x=150,y=340)  # To determine button's location


window.mainloop()  # If I don't click exit button the screen is not gonna close




























