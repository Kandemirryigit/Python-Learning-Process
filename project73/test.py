from tkinter import *

x = 2
y = 2
         
x_buttons=[]
for row in range(3):
            for col in range(3):
                x_button = Button(
                    text="X",
                    bg="black",
                    fg="black",
                    width=20,
                    height=9,
                )
                x_button.place(x=x, y=y)
                x_buttons.append(x_button)
                x += 150
            x = 2  # reset x after each row
            y+=150 

print(x_buttons[0])
print(x_buttons[1])
print(x_buttons[2])
print(x_buttons[3])







    # def click_x():

    #     x_label = Label(text="X", bg="black", fg="white", font=("Arial", 70, "bold"))
        
    #     if x_buttons[0]:
    #         x_label.place(x=40, y=20)
    #     elif x_buttons[1]:
    #         x_label.place(x=190, y=20)
    #     elif x_buttons[2]:
    #         x_label.place(x=340, y=20)
    #     elif x_buttons[3]:
    #         x_label.place(x=40, y=170)
    #     elif x_buttons[4]:
    #         x_label.place(x=190, y=170)
    #     elif x_buttons[5]:
    #         x_label.place(x=340, y=170)
    #     elif x_buttons[6]:
    #         x_label.place(x=40, y=320)
    #     elif x_buttons[7]:
    #         x_label.place(x=190, y=320)
    #     elif x_buttons[8]:
    #         x_label.place(x=340, y=320)








     # lines=[line1,line2,line3,line4]
    # if input("name: ")=="aa":
    #     for line in lines:
    #         canvas.itemconfig(line,fill="green")
        