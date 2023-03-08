from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def user_info():
    website = web_entry.get()
    email = user_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Is It Ok To Save?")
        if is_ok:
            # with open("data.json", "w") as data_file:
            #     json.dump(new_data, data_file, indent=4)
            try:
                with open("data.json", "r") as data_file:
                    # reading
                    data = json.load(data_file)
            except JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # saving or writing
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_input.delete(0, END)


def find_password():
    website = web_entry.get()
    with open("data.json", "r") as file_handle:
        content = json.load(file_handle)
        if website in content:
            email = content[website]["Email"]
            password = content[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Oops", message=f"No details for the {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=password_img)
canvas.grid(column=1, row=0)

web_entry = Entry(width=29)
web_entry.focus()
web_entry.grid(column=1, row=1)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_input = Entry(width=48)
user_input.insert(0, "xyz@gmail.com")
user_input.grid(column=1, row=2, columnspan=2)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_input = Entry(width=29)
password_input.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(width=41, text="Add", command=user_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=15, text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
