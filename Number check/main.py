from tkinter import *  # From tkinter import everything

window=Tk()  # To define tkinter
window.title("Number Check")  # To determine window's title
window.config(bg="#1D1616")  # To determine window's background color 
window.minsize(400,300)  # To determine window's size


# To create texts and determine their location,font,backgrouncolor,foregroundcolor
enter_number_text=Label(text="Enter Number:",font=("Monospace",12,"bold"),bg="#1D1616",fg="#8E1616")
enter_number_text.grid(column=1,row=2,pady=20)

prime_number_text=Label(text="Prime Number:",font=("Monospace",12,"bold"),bg="#1D1616",fg="white")
prime_number_text.grid(column=1,row=3,pady=20)

prime_number_result=Label(text="-",font=("Monospace",12,"bold"),bg="#1D1616",fg="#8E1616")
prime_number_result.grid(column=2,row=3)

perfect_number_text=Label(text="Perfect Number:",font=("Monospace",12,"bold"),bg="#1D1616",fg="white")
perfect_number_text.grid(column=1,row=4,pady=20)

perfect_number_result=Label(text="-",font=("Monospace",12,"bold"),bg="#1D1616",fg="#8E1616")
perfect_number_result.grid(column=2,row=4)

palindrom_number_text=Label(text="Palindrom Number:",font=("Monospace",12,"bold"),bg="#1D1616",fg="white")
palindrom_number_text.grid(column=1,row=5,pady=20)

palindrom_number_result=Label(text="-",font=("Monospace",12,"bold"),bg="#1D1616",fg="#8E1616")
palindrom_number_result.grid(column=2,row=5)


# To create an input and determine it's location
number_entry=Entry()
number_entry.focus()  # To add a blinking line in the input
number_entry.grid(column=2,row=2)


# To prime number
def prime_number():
    number=int(number_entry.get())
    remainders=[]  # To store remainders
    for i in range(2,number+1): # (include,exclude) because of that I wrote number+1
        remainder=number%i
        remainders.append(remainder)  # To add  list
   
    zero=remainders.count(0)
    if zero>1:
        prime_number_result.config(text="NO")
    elif number==0 or number==1:
        prime_number_result.config(text="NO")
    else:
        prime_number_result.config(text="YES")


def palindrom_number():
    number=number_entry.get()
    reversed_number=number[::-1]  # Reverse the number
    if number==reversed_number:
        palindrom_number_result.config(text="YES")
    else:
        palindrom_number_result.config(text="NO")


def perfect_number():
    number=int(number_entry.get())

    dividers=[]
    for i in range(1,number+1):  # (include,exclude) because of that I wrote number+1
        remainder=number%i
        if remainder==0 and i!=number: 
            dividers.append(i)  # To add

    result=0
    for i in range(len(dividers)):
        result+=dividers[i]

    if result==number:
        perfect_number_result.config(text="YES")
    else:
        perfect_number_result.config(text="NO")


def check_all():
    prime_number()
    palindrom_number()
    perfect_number()
    
    
# To create button and determine it's location,width,command
result_button=Button(text="Result",width=30,command=check_all)
result_button.grid(column=2,row=6)


window.mainloop()  # If I don't click exit button the screen won't close.