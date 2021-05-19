from tkinter import (
    Button,
    Canvas,
    Label,
    PhotoImage,
    Tk,
)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def setup_ui():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)
    
    timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    timer_label.grid(row=0, column=1)
    
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    start_button = Button(text="Start", highlightthickness=0)
    start_button.grid(row=2, column=0)

    start_button = Button(text="Reset", highlightthickness=0)
    start_button.grid(row=2, column=2)

    timer_label = Label(text="✔", fg=GREEN, bg=YELLOW)
    timer_label.grid(row=3, column=1)
    return window, canvas, timer_text


def count_down(window, count, canvas, timer_text):
    if count > 0:
        canvas.itemconfig(timer_text, text=count)
        window.after(1000, count_down, window, count - 1, canvas, timer_text)


window, canvas, timer_text = setup_ui()
count_down(window, 10, canvas, timer_text)
window.mainloop()
