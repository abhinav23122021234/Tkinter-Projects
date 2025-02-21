from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text,text=count)
    if count>0:
     window.after(1000,count_down,count-1)








# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)



title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,),bg=YELLOW)
title_label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato)
timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
count_down(5)

start_button=Button(text="Start")
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset")
reset_button.grid(column=2,row=2)



check_mark=Label(text="",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()