import tkinter
from tkinter import *
from tkinter import messagebox

user_data = {}


def store_data():
    website_get = website.get()

    if not website_get:
        print("Website can't be empty")
        messagebox.askokcancel(title="Title", message=f"website can't be empty")
    username_email_get = username_email.get()
    if not username_email_get:
        print("username can't be empty")
        messagebox.askokcancel(title="Title", message=f"username can't be empty")
    password_get = password.get()
    if not password_get:
        print("password can't be empty")
        messagebox.askokcancel(title="Title", message=f"password can't be empty")

    # user_data.update({username_email_get: [website_get, password_get]})
    is_ok = messagebox.askokcancel(title="Title", message=f"These are the details entered \n Email:{website_get} \n username:{username_email_get} \n password:{password_get}")

    if is_ok and website_get and username_email_get and password_get:
        with open('data.txt', mode='a+') as d_txt:
            d_txt.write(website_get)
            d_txt.write(' | ')
            d_txt.write(username_email_get)
            d_txt.write(' | ')
            d_txt.write(password_get)
            d_txt.write('\n')

    website.delete(0, END)
    username_email.delete(0, END)
    password.delete(0, END)
    return


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

username_email = tkinter.Entry(window, width=43)
username_email.grid(column=1, row=2, columnspan=3, sticky='w')
username_email.insert(0, "szymon@gmail.com")


password = tkinter.Entry(window, width=21)
password.grid(column=1, row=3, sticky='w')


button2 = tkinter.Button(text='Add', width=36, command=store_data)
button2.grid(column=1, row=4, columnspan=2, sticky='w')
window.mainloop()

