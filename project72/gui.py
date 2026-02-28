import pandas as pd
from tkinter import *
from tkinter import messagebox


BASE_PATH="C:/Users/CASPER/Desktop/python_projects/project72/"
CSV_PATH=BASE_PATH+"mors_alphabet.csv"
IMAGE_PATH=BASE_PATH+"image.png"



def run_gui():
    window=Tk()  # To define tkinter
    window.title("Morse Code Converter")  # To determine window's title
    window.config(bg="black",padx=30) # To determine window's backgroundcolor and padding
    window.minsize(800,600) # To determine window's size

    # To add image in the screen
    canvas=Canvas(width=210,height=150,bg="black",highlightthickness="0")  # Highlightthickness=0 delete borders 
    # This path won't work in your computer.You should write yours
    morse_code_img=PhotoImage(file=IMAGE_PATH)
    canvas.create_image(110,120,image=morse_code_img)
    canvas.place(x=260,y=80)

    # To create texts  and determine their location,backgroundcolor,foregroundcolor,font
    convert_label=Label(text="Convert:",bg="black",fg="white",font=("Arial",18,"bold"))
    convert_label.place(x=90,y=300)

    Result_label=Label(text="Result:",bg="black",fg="white",font=("Arial",18,"bold"))
    Result_label.place(x=107,y=360)

    result_text=Label(text="",bg="black",fg="white",font=("Arial",20,"bold"))
    result_text.place(x=220,y=360)

    # To create an input and determine it's location,backgroundcolor,foregroundcolor,font,wdth
    convert_entry=Entry(bg="white",fg="black",font=("Arial",15,"bold"),width="30")
    convert_entry.place(x=210,y=305)
    convert_entry.focus()  # To add a blinking cursor in the input


    def copy():
         copied_text=result_text.cget("text")
         window.clipboard_clear()
         window.clipboard_append(copied_text)
         messagebox.showinfo(title="Error",message="copied")
        

    copy_button=convert_button=Button(text="Copy",bg="white",fg="black",width=10,command=copy)
    copy_button.place(x=550,y=365)

    def clear():
         result_text.config(text=" ")

    clear_button=convert_button=Button(text="Clear",bg="white",fg="black",width=10,command=clear)
    clear_button.place(x=640,y=365)


    def convert_button():
            
            try: 
        
                df1=pd.read_csv(CSV_PATH)
                letters=convert_entry.get().upper()

                output=""
                for letter in letters:
                    result=df1[df1["chars"]==letter]["morse_code"].iloc[0]
                    output+=result+" "

                result_text.config(text=output) # To add output in the screen

                if not letters:
                    messagebox.showinfo(title="Error",message="The entry cannot be empty.")
               
                    
            except:  
                messagebox.showinfo(title="Error",message=f"'{letter}' letter is not in the morse alphabet...")
                
                
    # To create a button and determine it's location,backgroundcolor,foregroundcolor,width and command
    convert_button=Button(text="convert",bg="white",fg="black",width=60,command=convert_button)
    convert_button.place(x=150,y=430)


    window.mainloop()  # If I don't click exit button the screen won't close

