from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

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
email_entry = Entry(width=45)
password_entry = Entry(width=35)

website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry.grid(column=1, row=3, sticky=W)

password_button = Button(text="Generate", bg="white")
password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=38, bg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
