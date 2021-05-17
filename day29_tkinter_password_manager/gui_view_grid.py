from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 12, 'bold')


# ---------------------------- UI SETUP ------------------------------- #
class GuiView:
    def __init__(self, search, generate_password, save):
        self.window = Tk()
        self.window.title('Password Manager')
        self.window.config(padx=50, pady=50)
        self.window.minsize(width=650, height=450)

        self.label_website = Label(text='Website:', font=FONT)
        self.label_email = Label(text='Email/Username:', font=FONT)
        self.label_password = Label(text='Password:', font=FONT)
        self.label_website.grid(column=0, row=1)
        self.label_email.grid(column=0, row=2)
        self.label_password.grid(column=0, row=3)

        self.entry_website = Entry(width=35)
        self.entry_email = Entry(width=35)
        self.entry_password = Entry(width=35)

        self.entry_website.grid(column=1, row=1, columnspan=1)
        self.entry_email.grid(column=1, row=2, columnspan=1)
        self.entry_password.grid(column=1, row=3, columnspan=1)

        self.entry_website.focus()

        self.entry_email.insert(0, 'name@email.com')

        self.button_search = Button(text="Search", command=search, width=17)
        self.button_generate = Button(text='Generate Password', command=generate_password, width=17)
        self.button_generate.grid(column=3, row=3, columnspan=1)
        self.button_add = Button(text='Add', command=save, width=30)
        self.button_search.grid(column=3, row=1, columnspan=1)
        self.button_add.grid(column=1, row=4, columnspan=1)

        self.logo = PhotoImage(file='logo.png')

        self.canvas = Canvas(width=220, height=200)
        self.image = self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(column=1, row=0)