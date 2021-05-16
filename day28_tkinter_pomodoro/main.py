from tkinter import *
# import main
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = u'\u2713'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global canvas
    global window
    global timer_text
    mins = f"{int(count / 60)}".zfill(2)
    secs = f"{count % 60}".zfill(2)
    time_display = f"{mins.zfill(2)}:{secs.zfill(2)}"
    canvas.itemconfig(timer_text, text=time_display)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            marks += CHECK
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)



start_button = Button(text='Start', command=start_timer)
reset_button = Button(text='Reset', command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_label = Label(text='', font=(FONT_NAME, 16, 'bold'), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()