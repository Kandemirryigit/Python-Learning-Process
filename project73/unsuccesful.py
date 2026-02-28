from tkinter import *
from tkinter import messagebox
import time





def game():
    global clicked,turn,all_o,all_x

    if new_color_x=="green":
        turn="X"
    elif new_color_o=="green":
         turn="O" 
    

    
    window=Tk()
    window.title("Tic-Toc Game")
    window.config(bg="Black")
    window.minsize(450,490)
    
    canvas=Canvas(window,width=450,height=450,bg="black")
    canvas.pack()

    canvas.create_line(0,150,500,150,width=5,fill="red"),
    canvas.create_line(0,300,500,300,width=5,fill="red"),
    canvas.create_line(150,0,150,450,width=5,fill="red"),
    canvas.create_line(300,0,300,450,width=5,fill="red"),

    back_button=Button(text="<<< Back",bg="black",fg="red",width=57,height=2,font=("Monospace",10,"bold"))
    back_button.place(x=0,y=445)

    
    game_logic()

    window.mainloop()






def game_logic():
    global clicked
    
    clicked=False
    def click_x(row,column):
        global clicked

        if clicked:
            return
        
        clicked=True

        x_label = Label(text="X", bg="black", fg="white", font=("Arial", 70, "bold"))
        
        if row==0 and column==0:
            x_label.place(x=40, y=20)
        elif row==0 and column==1:
            x_label.place(x=190, y=20)
        elif row==0 and column==2:
            x_label.place(x=340, y=20)
        elif row==1 and column==0:
            x_label.place(x=40, y=170)
        elif row==1 and column==1:
            x_label.place(x=190, y=170)
        elif row==1 and column==2:
            x_label.place(x=340, y=170)
        elif row==2 and column==0:
            x_label.place(x=40, y=320)
        elif row==2 and column==1:
            x_label.place(x=190, y=320)
        elif row==2 and column==2:
            x_label.place(x=340, y=320)
          

    def all_x():
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
                        command=lambda r=row, c=col: click_x(r, c)
                    )
                    x_button.place(x=x, y=y)
                    x_buttons.append(x_button)
                    x += 150
                x = 2  # reset x after each row
                y+=150
    










    def click_o(row,column):
        global clicked

        if clicked:
            return
        
        clicked=True

        x_label = Label(text="O", bg="black", fg="white", font=("Arial", 70, "bold"))
        
        if row==0 and column==0:
            x_label.place(x=40, y=20)
        elif row==0 and column==1:
            x_label.place(x=190, y=20)
        elif row==0 and column==2:
            x_label.place(x=340, y=20)
        elif row==1 and column==0:
            x_label.place(x=40, y=170)
        elif row==1 and column==1:
            x_label.place(x=190, y=170)
        elif row==1 and column==2:
            x_label.place(x=340, y=170)
        elif row==2 and column==0:
            x_label.place(x=40, y=320)
        elif row==2 and column==1:
            x_label.place(x=190, y=320)
        elif row==2 and column==2:
            x_label.place(x=340, y=320)

    def all_o():
        x = 2
        y = 2
        o_buttons=[]
        for row in range(3):
                for col in range(3):
                    x_button = Button(
                        text="O",
                        bg="black",
                        fg="black",
                        width=20,
                        height=9,
                        command=lambda r=row, c=col: click_o(r, c)
                    )
                    x_button.place(x=x, y=y)
                    o_buttons.append(x_button)
                    x += 150
                x = 2  # reset x after each row
                y+=150

    if new_color_x=="green":
        turn="X"
    else:
        turn="O"


    if turn=="X":
                all_x()
                
            
    elif turn=="O":
                all_o()
                turn="X"


    







   






   



    
        
    






    
                       
                        




             
   


  



    

    
        



   
   










def start_screen():
    global new_color_o,new_color_x
    start_window=Tk()
    start_window.title("Tic-Toc Game")
    start_window.config(bg="Black")
    start_window.minsize(450,450)

    welcome_label=Label(text="Welcome",bg="black",fg="white",font=("Monospace",24,"bold"))
    welcome_label.place(x=150,y=50)

    tic_toc_game_label=Label(text="Tic-Toc Game",bg="black",fg="white",font=("Arial",24,"bold"))
    tic_toc_game_label.place(x=110,y=120)

    chrachter_label=Label(text="Which Chracter You Wanna Be?",bg="black",fg="white",font=("Arial",12,"bold"))
    chrachter_label.place(x=90,y=200)

    def x_button_click():
        current_colorx= x_button.cget("bg")
        if current_colorx == "white":
            x_button.config(bg="green")
        else:
            x_button.config(bg="white")

    def o_button_click():
        current_coloro = o_button.cget("bg")
        if current_coloro == "white":
            o_button.config(bg="green")
        else:
            o_button.config(bg="white")



    def contiune_button_clicked():
        global new_color_x,new_color_o
        new_color_x=x_button.cget("bg")
        new_color_o=o_button.cget("bg")

        if new_color_o==new_color_x:  
                messagebox.showinfo(title="Error",message="Please Choose one of them!")
        else:
            start_window.destroy()
            game()
        

    x_button=Button(text="X",bg="white",fg="black",width=10,command=x_button_click)
    x_button.place(x=100,y=250)

    or_label=Label(text="or",bg="black",fg="white",font=("Arial",12,"bold"))
    or_label.place(x=210,y=250)

    o_button=Button(text="O",bg="white",fg="black",width=10,command=o_button_click)
    o_button.place(x=260,y=250)


    contiune_button=Button(text="Contiune",bg="white",fg="black",width=15,command=contiune_button_clicked)
    contiune_button.place(x=160,y=300)

   
    start_window.mainloop()
    


start_screen()









































