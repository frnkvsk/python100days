from tkinter import *
import pandas
import random
# -------------------------- CONSTANTS ------------------------------#
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
DELAY = 3000

# -------------------------- UI SETUP  ------------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


class GuiView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.window.minsize(width=900, height=726)
        self.CARD_FRONT = PhotoImage(file="images/card_front.png")
        self.CARD_BACK = PhotoImage(file="images/card_back.png")
        self.CROSS_IMAGE = PhotoImage(file="images/wrong.png")
        self.CHECK_IMAGE = PhotoImage(file="images/right.png")
        self.canvas = Canvas(width=800, height=526)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.image = self.canvas.create_image(400, 263, image=self.CARD_FRONT)
        self.current_choice = 0
        self.title = self.canvas.create_text(400, 150, text="", font=FONT_TITLE)
        self.word = self.canvas.create_text(400, 263, text="", font=FONT_WORD)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_button = Button(image=self.CROSS_IMAGE, highlightthickness=0, command=self.next_card)
        self.cross_button.grid(row=1, column=0)
        self.check_button = Button(image=self.CHECK_IMAGE, highlightthickness=0, command=self.is_known)
        self.check_button.grid(row=1, column=1)
        self.new_word = {}
        self.flip_timer = self.canvas.after(DELAY, self.next_card)

    def flip_card(self):
        self.canvas.itemconfig(self.image, image=self.CARD_BACK)
        self.canvas.itemconfig(self.title, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=self.new_word["English"], fill="white")

    def next_card(self):
        print(len(to_learn))
        self.window.after_cancel(self.flip_timer)
        self.new_word = random.choice(to_learn)
        self.canvas.itemconfig(self.image, image=self.CARD_FRONT)
        self.canvas.itemconfig(self.title, text="French", fill="black")
        self.canvas.itemconfig(self.word, text=self.new_word["French"], fill="black")
        self.flip_timer = self.canvas.after(DELAY, self.flip_card)

    def is_known(self):
        to_learn.remove(self.new_word)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()
