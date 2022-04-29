import random
import string
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genpsw() -> str:
    password_entry.delete(0, END)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation
    all = lower + upper + nums + symbols
    psw = random.sample(all, 8)
    password = "".join(psw)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not (password and website and email):
        print("please fill all fields")
    else:
        # print(website, email, password)
        with open("data.txt", mode="a") as file:
            data = f'{website} | {email} | {password} \n'
            file.write(data)
            print("password saved")


# ---------------------------- UI SETUP ------------------------------- #
# website, email, password = None
window = Tk()
window.config(padx=40, pady=20)
window.minsize(width=400, height=400)
window.title("Password mannager")

logo = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200, height=200)
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(column=1, row=0, sticky=W)

website_label = Label(text="Website :")
email_label = Label(text="Email/Username :")
password_label = Label(text="Password :")

website_label.grid(column=0, row=1, sticky=W)
email_label.grid(column=0, row=2, sticky=W)
password_label.grid(column=0, row=3, sticky=W)

website_entry = Entry(width=45)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=35)

website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry.grid(column=1, row=3, sticky=W)

password_button = Button(text="Generate", bg="white", command=lambda: password_entry.insert(0, genpsw()))
password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=38, bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
