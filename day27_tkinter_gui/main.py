from tkinter import *

import main

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)
result = '0'


def button_clicked():
    miles = input.get()
    km = int(float(miles) * 1.609)
    main.label_result.config(text=km)


input = Entry(width=10)
input.grid(column=1, row=0)

label = Label(text='Miles', font=('Arial', 16, 'normal'))
label.grid(column=2, row=0)
label.config(padx=5)

label2 = Label(text='is equal to', font=('Arial', 16, 'normal'))
label2.grid(column=0, row=1)

label_result = Label(text=result, font=('Arial', 16, 'normal'))
label_result.grid(column=1, row=1)

label_km = Label(text='Km', font=('Arial', 16, 'normal'))
label_km.grid(column=2, row=1)

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()