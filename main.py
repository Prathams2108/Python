from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label1.config(text="Timer")
    label2.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    reps +=1

    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        label1.config(text="Long Break", font=(FONT_NAME, 24, "bold"), fg=PINK, bg=RED)
        countdown(work_sec)
    elif reps%2==0:
        label1.config(text="Short Break", font=(FONT_NAME, 24, "bold"), fg=YELLOW, bg=RED)
        countdown(short_sec)
    else:
        label1.config(text="Working", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=RED)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=RED)


canvas=Canvas(width=200, height=224, bg=RED, highlightthickness=0)
tomato_png=PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
timer_text=canvas.create_text(103, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#Timer Label
label1=Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=RED)
label1.grid(row=0, column=1)

label2=Label(font=(FONT_NAME, 12), fg=GREEN,bg=RED)
label2.grid(row=4, column=1)
#Buttons
start_button=Button(text="Start", height=1, width=8, highlightthickness=0, command=start_timer)
start_button.grid(row=4, column=0)

reset_button=Button(text="Reset", height=1, width=8, highlightthickness=0, command=reset_timer)
reset_button.grid(row=4, column=2)
window.mainloop()