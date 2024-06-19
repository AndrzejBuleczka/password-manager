from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.config(bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.config(bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.config(bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.config(bg="white")
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
# website_input.focus()
email_input = Entry(width=35)
email_input.config(bg="white")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
# email_input.insert(0, "5bLbF@example.com")
password_input = Entry(width=21)
password_input.config(bg="white")
password_input.grid(row=3, column=1, sticky="EW")


password_generator_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_generator_button.config(bg="white")
password_generator_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_button.config(bg="white")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
