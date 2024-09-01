import tkinter
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)
# window.geometry('200x200')

logo_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(80, 100, image=logo_image)
canvas.grid(column=1, row=0, sticky='w')

label1 = tkinter.Label(text='Website:')
label1.grid(column=0, row=1)

label2 = tkinter.Label(text='Email/Username:')
label2.grid(column=0, row=2)

label3 = tkinter.Label(text='Password:')
label3.grid(column=0, row=3)

button1 = tkinter.Button(text='Generate Password')
button1.grid(column=2, row=3, sticky='w')

button2 = tkinter.Button(text='Add', width=36)
button2.grid(column=1, row=4, columnspan=3, sticky='w')

input_website = tkinter.Entry(window, width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky='w')

input_username_email = tkinter.Entry(window, width=35)
input_username_email.grid(column=1, row=2, columnspan=2, sticky='w')

input_password = tkinter.Entry(window, width=21)
input_password.grid(column=1, row=3, columnspan=2, sticky='w')
window.mainloop()

