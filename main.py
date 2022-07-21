import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0
reps = 0
timer_for_reset = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer_for_reset)
    canvas.itemconfig(timer, text="00:00")
    tick_mark.config(text="")
    timer_txt.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    global reps
    reps += 1
    print(reps)
    
    if reps % 2 != 0 and reps <= 7:
        timer_txt.config(text="Work", foreground=GREEN)
        count_down(WORK_MIN * 60) 
    elif reps % 2 == 0 and reps <= 6:
        timer_txt.config(text="Break", foreground=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 8 == 0:
        timer_txt.config(text="Break", foreground=RED)
        count_down(LONG_BREAK_MIN * 60)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    
    if count > 0:
       global timer_for_reset 
       timer_for_reset = window.after(1000, count_down, count - 1)
    else:
        check_mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            check_mark += "✔"
        tick_mark.config(text=check_mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_txt = tkinter.Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 50, "bold"), background=YELLOW)
timer_txt.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", font=("Arial", 10 ), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", font=("Arial", 10 ), command=reset)
reset_button.grid(row=2, column=2)

tick_mark = tkinter.Label(text="", foreground=GREEN, background=YELLOW, font=("Arial", 15,"bold"))
tick_mark.grid(row=3, column=1)

window.mainloop()