from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="The name of  is too short", message="please input your info")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file , indent=4)

        else:
            # Updateing old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
   website = website_entry.get()
   try:
       with open("data.json") as data_file:
           data = json.load(data_file)
   except FileNotFoundError:
       messagebox.showinfo(title="Error", message="No data file found.")
   else:
       if website in data:
           email = data[website]["email"]
           password = data[website]["password"]
           messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
       else:
           messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


    # if len(website) == 0:
    #     messagebox.showinfo(title="There is no website name", message="please input your info")
    # else:
    #     try:
    #         with open("data.json", 'r') as data_file:
    #             data = json.load(data_file)
    #             print(data[website]['password'])
    #             messagebox.showinfo(title=f"{data[website]}", message=f"website: {website},\n Password: {data[website]['password']}")
    #     except KeyError:
    #         messagebox.showinfo(title=f"{website} is not exitst", message=f"{website} is not exitst")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
# Entries

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, "jisung.smart@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=13 , command = find_password)
search_button.grid(row=1, column=2)

window.mainloop()
