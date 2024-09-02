import tkinter
from tkinter import *


def store_data(web, username, passwd):
    user_data = {}
    user_data.update({username: [web, passwd]})
    print(user_data)
    return


def print_data(test_arg):
    print('test', test_arg)


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
button1.grid(column=1, row=3, columnspan=3, ipadx=11, sticky='e')


website = tkinter.Entry(window, width=43)
website.grid(column=1, row=1, columnspan=3, sticky='w')
website.focus()
website_get = website.get()

username_email = tkinter.Entry(window, width=43)
username_email.grid(column=1, row=2, columnspan=3, sticky='w')
username_email.insert(0, "szymon@gmail.com")
username_email_get = username_email.get()

password = tkinter.Entry(window, width=21)
password.grid(column=1, row=3, sticky='w')
password_get = password.get()

action_with_arg = print_data(1)
button2 = tkinter.Button(text='Add', width=36, command=action_with_arg)
button2.grid(column=1, row=4, columnspan=2, sticky='w')
window.mainloop()

