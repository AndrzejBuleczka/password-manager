from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_input.delete(0, END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(title="Success", message="Password has been saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

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
website_input.focus()
email_input = Entry(width=35)
email_input.config(bg="white")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "yourEmail@example.com")
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
