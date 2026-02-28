from tkinter import *  # rom tkinter import everything

window=Tk()  # To define tkinter
window.minsize(400,350)  # To determine window's size
window.title("Seconds Converter")  # To determine window's title

seconds_converter_text=Label(text="Seconds converter",font=("Arial",12,"underline"),fg="red") # to create a text
seconds_converter_text.place(x=110,y=30) # To determine text's location

seconds_text=Label(text="Seconds:",font=("Arial",12,"bold"))
seconds_text.place(x=115,y=100)

time_text=Label(text="hours:minutes:seconds :",font=("Arial",12,"bold"))
time_text.place(x=5,y=150)

result_text=Label(text="0",font=("Arial",12,"bold"))
result_text.place(x=230,y=150)

seconds=Entry()  # To create an input
seconds.place(x=200,y=103)  # To determine input's location


def button_clicked():
    hour=int(seconds.get())//3600
    minute=int((int(seconds.get())-(hour*3600))/60)
    second=(int(seconds.get())-(minute*60))%60
    result_text.config(text=f"{hour}:{minute}:{second}")


calculate_button=Button(text="Calculate",command=button_clicked, width=25,height=1)  # To create a button
calculate_button.place(x=120,y=215)  # To determine button's location

































window.mainloop()
