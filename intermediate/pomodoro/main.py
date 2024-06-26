from tkinter import *
import math

# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer  = None

# TIMER RESET 

def cancel_timer():
    global reps
    window.after_cancel(timer)
    check_marks.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# TIMER MECHANISM 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Focus", fg=GREEN)

# COUNTDOWN MECHANISM 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔️"
        check_marks.config(text=mark)

# UI Setup

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#title
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

#canvas
canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(103,80, image=my_image)
timer_text = canvas.create_text(103,90, font=(FONT_NAME, 35, "bold"), fill="white", text="00:00")
canvas.grid(column=1, row=1)


#buttons
start_btn = Button(text="Start", highlightthickness=0 , command=start_timer)
start_btn.grid(column=0, row=2)

end_btn = Button(text="Reset", highlightthickness=0, command=cancel_timer)
end_btn.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()