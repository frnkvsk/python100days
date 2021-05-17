from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ------ change between grid and place gui render ------------------
# from gui_view_placeXY import GuiView
from gui_view_grid import GuiView

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 12, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(numbers) for _ in range(randint(2, 4))] + \
                    [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #


def search():
    website = entry_website.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't Website field empty.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                if website in data:
                    pyperclip.copy(data[website]['password'])
                    messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
                else:
                    messagebox.showinfo(title=website, message=f"Website {website} is not on record yet.")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"No Data File Found.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get().lower()
    email = entry_email.get().lower()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=5)
                entry_website.delete(0, END)
                entry_password.delete(0, END)
        else:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=5)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


gui = GuiView(search, generate_password, save)
window = gui.window
entry_website = gui.entry_website
entry_email = gui.entry_email
entry_password = gui.entry_password

window.mainloop()