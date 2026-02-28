import pandas  # We use pandas to data manipulation and analysis
# To create user interface we use tkinter
from tkinter import *  # From tkinter import everything
from tkinter import messagebox  # to use messagebox 

window=Tk()  # To define tkinter
window.title("Nato Phonetic Alphabet")  # To determine window's title
window.config(bg="black",padx=30) # To determine window's backgroundcolor and padding
window.minsize(800,600) # To determine window's size

# To add image in the screen
canvas=Canvas(width=230,height=200,bg="black",highlightthickness="0")  # Highlightthickness=0 delete borders 
# This path won't work in your computer.You should write yours
phonetic_alphabet_img=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/Nato Phonetic Alphabet/nato phonetic alphabet.png")
canvas.create_image(110,120,image=phonetic_alphabet_img)
canvas.place(x=260,y=50)

# To create texts  and determine their location,backgroundcolor,foregroundcolor,font
enter_name_label=Label(text="Enter Name:",bg="black",fg="white",font=("Arial",18,"bold"))
enter_name_label.place(x=50,y=300)

Result_label=Label(text="Result:",bg="black",fg="white",font=("Arial",18,"bold"))
Result_label.place(x=107,y=360)

result_text=Label(text="",bg="black",fg="white",font=("Arial",10,"bold"))
result_text.place(x=220,y=368)


# To create an input and determine it's location,backgroundcolor,foregroundcolor,font,wdth
enter_name_entry=Entry(bg="white",fg="black",font=("Arial",15,"bold"),width="40")
enter_name_entry.place(x=210,y=305)
enter_name_entry.focus()  # To add a blinking cursor in the input


def convert_button():
        
        try: # Try this codes
            data=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/Nato Phonetic Alphabet/nato_phonetic_alphabet.csv")
            # Itterrows is a Pandas function that allows you to iterate over a DataFrame row by row.
            phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
            word=enter_name_entry.get().upper()  # Whatever you write is all going to be uppercase
            output_list=[phonetic_dict[letter] for letter in word]
            result_text.config(text=output_list) # To add output in the screen
        except KeyError:  # If keyerror occurs
              # If keyerror occurs we are gonna see this pop-up in the screen
              messagebox.showinfo(title="info",message="you can't use anything else except English alphabet")
              
            
# To create a button and determine it's location,backgroundcolor,foregroundcolor,width and command
convert_button=Button(text="convert",bg="white",fg="black",width=60,command=convert_button)
convert_button.place(x=150,y=430)


window.mainloop()  # If I don't click exit button the screen won't close



