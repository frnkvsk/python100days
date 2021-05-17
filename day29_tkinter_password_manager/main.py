from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
window.minsize(width=550, height=450)

label_website = Label(text='Website:', font=FONT)
label_email = Label(text='Email/Username:', font=FONT)
label_password = Label(text='Password:', font=FONT)
label_website.grid(column=0, row=1)
label_email.grid(column=0, row=2)
label_password.grid(column=0, row=3)

entry_website = Entry(width=43)
entry_email = Entry(width=43)
entry_password = Entry(width=21)

entry_website.place(x=140, y=206)
entry_email.place(x=140, y=231)
entry_password.place(x=140, y=256)

entry_website.focus()

entry_email.insert(0, 'name@email.com')
button_generate = Button(text='Generate Password', command=generate_password, width=17, justify=LEFT).place(x=273, y=252)
button_add = Button(text='Add', command=save, width=36, justify=LEFT).place(x=140, y=280)

logo = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
image = canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()