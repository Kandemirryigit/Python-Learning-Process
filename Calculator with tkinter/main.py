from tkinter import *   # from tkinter import everything
import re   # It provides functions for searching, matching, and manipulating strings based on patterns.

window = Tk()  # To define tkinter
window.title("Calculator")  # To determine window's title
window.minsize(320, 350)   # To determine window's size
window.config(bg="black")  # To determine window's background color


# To push all content to the bottom
window.grid_rowconfigure(0, weight=1)  # Expands row 0 to push content down


def extract_numbers():
   global first_number, second_number  # We are inside a function and if we want to use this variables inside another function we should use this method
  
   expression = number_top.cget("text")   # Get text
   numbers = re.findall(r'-?\d+\.\d+|-?\d+' , expression)  # To extract numbers from text
   if len(numbers) >= 2:
        first_number = float(numbers[0]) 
        second_number = float(numbers[1]) 
        return True
   return False  



def append_text(button):   # I added button parameter because I have lots of button and I wanted to create a shortcut
    present=number_top.cget("text")
    new=present+button.cget("text")
    number_top.config(text=new)

def c():
    # To clear screen
    number_top.config(text="")
    number.config(text="")


def equal(): 
    if not extract_numbers():
        number.config(text="Error")
        return
    
    expression=number_top.cget("text")

    if "+" in expression:
        result= first_number + second_number
    elif " − " in expression:
        result= first_number - second_number
    elif "x" in expression:
        result= first_number * second_number
    elif "/" in expression:
        if second_number==0:
            number.config(text="Math Error")
            return
        result= first_number / second_number
    elif "^" in expression:
        result= first_number ** second_number
    elif "%" in expression:
        result=(first_number*second_number)/100
    elif "mod" in expression:
        result=first_number%second_number
    
    number_top.config(text="")
    number.config(text=result)

  


# Buttons layout (starting from row 10)

# I used lambda here because I wanted to give various things inside function
button1 = Button(text="1", width=10, height=3,bg="black",fg="White",font=("Sans-serif",9,"bold"),command=lambda:append_text(button1))
button1.grid(column=1, row=10)

button2 = Button(text="2", width=10, height=3,bg="black",fg="white",font=("Sans-serif",9,"bold"),command=lambda:append_text(button2))
button2.grid(column=2, row=10,)

button3 = Button(text="3", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button3))
button3.grid(column=3, row=10,)

button4 = Button(text="4", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button4))
button4.grid(column=1, row=11,)

button5 = Button(text="5", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button5))
button5.grid(column=2, row=11,)

button6 = Button(text="6", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button6))
button6.grid(column=3, row=11,)

button7 = Button(text="7", width=10, height=3,bg="black",fg="white",font=("Sans-serif",9,"bold"),command=lambda:append_text(button7))
button7.grid(column=1, row=12,)

button8 = Button(text="8", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button8))
button8.grid(column=2, row=12,)

button9 = Button(text="9", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button9))
button9.grid(column=3, row=12,)

button0 = Button(text="0", width=10, height=3,bg="black",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button0))
button0.grid(column=2, row=13,)



button_c = Button(text="c", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=c)
button_c.grid(column=1, row=13,)

button_point = Button(text=".", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button_point))
button_point.grid(column=3, row=13, )  # Bottom-left corner

button_div = Button(text="/", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button_div))
button_div.grid(column=5, row=9, )

button_perc = Button(text="%", width=10, height=3,bg="white",fg="black",font=("Monospace",9,"bold"),command=lambda:append_text(button_perc))
button_perc.grid(column=2, row=9, )

button_base = Button(text="^", width=10, height=3,bg="white",fg="black",font=("Monospace",9,"bold"),command=lambda:append_text(button_base))
button_base.grid(column=3, row=9, )

button_mod = Button(text="mod", width=10, height=3,bg="white",fg="black",font=("Sans-serif",9),command=lambda:append_text(button_mod))
button_mod.grid(column=1, row=9,)

button_plus = Button(text="+", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button_plus))
button_plus.grid(column=5, row=10,)

button_extract = Button(text=" − ", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button_extract))
button_extract.grid(column=5, row=11,)

button_mult = Button(text="x", width=10, height=3,bg="orange",fg="white",font=("Monospace",9,"bold"),command=lambda:append_text(button_mult))
button_mult.grid(column=5, row=12,)

button_equal = Button(text="=", width=10, height=3,bg="white",fg="black",font=("Monospace",9,"bold"),command=equal)
button_equal.grid(column=5, row=13,)

number_top=Label(text="",font=("Monospace",9,"bold"),bg="black",fg="white")
number_top.grid(column=5,row=0)

number=Label(text="",font=("Monospace",9,"bold"),bg="black",fg="white")
number.grid(column=5,row=1)

window.mainloop()   # If I don't click exit the window won't close.



