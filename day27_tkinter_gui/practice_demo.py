from tkinter import *


window = Tk()
window.title('My GUI')
window.minsize(width=800, height=500)
window.config(padx=50, pady=50)


def button_clicked():
    print('button clicked')

# Label
my_label = Label(text='Label', font=('Arial', 24, 'bold'))
my_label2 = Label(text='New Label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label2.grid(column=2, row=0)


# Button
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=20)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()