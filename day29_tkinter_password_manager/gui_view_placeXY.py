from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 12, 'bold')


# ---------------------------- UI SETUP ------------------------------- #
class GuiView:
    def __init__(self, search, generate_password, save):
        self.window = Tk()
        self.window.title('Password Manager')
        self.window.config(padx=50, pady=50)
        self.window.minsize(width=550, height=450)

        self.label_website = Label(text='Website:', font=FONT)
        self.label_email = Label(text='Email/Username:', font=FONT)
        self.label_password = Label(text='Password:', font=FONT)
        self.label_website.grid(column=0, row=1)
        self.label_email.grid(column=0, row=2)
        self.label_password.grid(column=0, row=3)

        self.entry_website = Entry(width=21)
        self.entry_email = Entry(width=43)
        self.entry_password = Entry(width=21)

        self.entry_website.place(x=140, y=206)
        self.entry_email.place(x=140, y=231)
        self.entry_password.place(x=140, y=256)

        self.entry_website.focus()

        self.entry_email.insert(0, 'name@email.com')

        self.button_search = Button(text="Search", command=search, width=17).place(x=273, y=201)
        self.button_generate = Button(text='Generate Password', command=generate_password, width=17, justify=LEFT).place(x=273, y=252)
        self.button_add = Button(text='Add', command=save, width=36, justify=LEFT).place(x=140, y=280)

        self.logo = PhotoImage(file='logo.png')

        self.canvas = Canvas(width=200, height=200)
        self.image = self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(column=1, row=0)