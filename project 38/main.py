from tkinter import *
import math



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK= "#09122C"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None




def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%2==1:
        count_down(work_sec)
        timer_label.config(text="Work Time",fg=GREEN)
    elif reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short Break",fg=PINK)
       
    


def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✅"
        check_marks.config(text="✅")
        check_marks.place(x=90+(reps*9.5),y=360)
    



def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_text,text="00:00")
    check_marks.config(text="")
    global reps
    reps=0



        
window=Tk()
window.title("Pomodoro")
window.minsize(600,600)
window.config(padx=100,pady=150,bg=YELLOW)
fg=GREEN




canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project 38/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,135,text="00:00",font=("Arial",35,"bold"))
canvas.place(x=100,y=0)




timer_label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
timer_label.place(x=120,y=-50)


start_button=Button(text="Start",font=("Arial",12,"bold"),command=start_timer)
start_button.place(x=40,y=250)


reset_button=Button(text="Reset",font=("Arial",12,"bold"),command=reset_timer)
reset_button.place(x=280,y=250)



check_marks=Label(bg=YELLOW,fg=GREEN)
check_marks.place(x=180,y=260)


start_point=Label(text="||",bg=YELLOW,fg=BLACK,font=("Arial",15,"bold"))
start_point.place(x=90,y=350)

end_point1=Label(text="||",bg=YELLOW,fg=BLACK,font=("Arial",15,"bold"))
end_point1.place(x=170,y=350)

end_point2=Label(text="||",bg=YELLOW,fg=BLACK,font=("Arial",15,"bold"))
end_point2.place(x=250,y=350)





window.mainloop()























