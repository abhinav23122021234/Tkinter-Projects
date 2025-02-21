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
REPS = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    REPS = 0
    timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS, timer

    if timer is not None:
        return  # if a timer is already running, do nothing

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break", fg=PINK)
    elif REPS % 2 == 0:
        count_down(short_break)
        title_label.config(text="Short Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work Mode", fg=GREEN)

    REPS += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = count // 60
    count_sec = str(count % 60)
    if len(count_sec)==1:
        count_sec="0"+count_sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Schedule next countdown
    else:
        timer = None
        start_timer()

        marks = "✔" * (REPS // 2)
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW,font=(FONT_NAME,25,"bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
