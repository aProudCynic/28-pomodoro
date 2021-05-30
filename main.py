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


class Period:

    def __init__(self, name, length_in_mins, color):
        self.name = name
        self.length_in_mins = length_in_mins
        self.color = color


periods = [
    Period('work', WORK_MIN, GREEN),
    Period('break', SHORT_BREAK_MIN, PINK),
] * 3 + [
    Period('work', WORK_MIN, GREEN),
    Period('break', LONG_BREAK_MIN, RED),
]
cycle = 0
remaining_seconds_in_period = None
timer_label = None
checkmark_label = None
countdown = None
timer_text = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def setup_ui():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    global timer_label
    timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    timer_label.grid(row=0, column=1)
    
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato)

    global timer_text
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    start_button = Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.grid(row=2, column=0)

    start_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
    start_button.grid(row=2, column=2)

    global checkmark_label
    checkmark_label = Label(fg=GREEN, bg=YELLOW)
    checkmark_label.grid(row=3, column=1)
    return window, canvas, timer_text


def _format_seconds(count):
    minutes = count // 60
    seconds = count % 60
    return f'{_at_least_two_digits(minutes)}:{_at_least_two_digits(seconds)}'


def _at_least_two_digits(number):
    return number if number >= 10 else "0" + str(number)


def count_down(window, canvas, timer_text):
    global remaining_seconds_in_period
    global cycle
    global checkmark_label
    global countdown
    is_initiated = remaining_seconds_in_period is None
    if not is_initiated and remaining_seconds_in_period <= 0:
        cycle += 1
    period = periods[cycle]
    if is_initiated or remaining_seconds_in_period <= 0:
        remaining_seconds_in_period = period.length_in_mins * 60
        timer_label.config(text=period.name, fg=period.color)
    if remaining_seconds_in_period > 0:
        formatted_time = _format_seconds(remaining_seconds_in_period)
        canvas.itemconfig(timer_text, text=formatted_time)
        remaining_seconds_in_period -= 1
        countdown = window.after(1000, count_down, window, canvas, timer_text)
    elif period.name == 'break':
        current_text = checkmark_label.cget("text")
        checkmark_label.config(text=f"{current_text}✔")


def start_timer():
    count_down(window, canvas, timer_text)


def reset_timer():
    global checkmark_label
    global timer_text
    global canvas
    window.after_cancel(countdown)
    timer_label.config(text="timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label = ""


window, canvas, timer_text = setup_ui()
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
