from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    search_for = website_entry.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data =json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='File Not Found', message='No Data File Found.')

    if search_for in data:
        messagebox.showinfo(title='Info Found', message=f'Email: {data[search_for]['email']}\n'
                                                        f'Password: {data[search_for]['password']}\n')
    else:
        messagebox.showerror(title='Info Not Found', message='No details for the website exists.')



def capture_info():
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
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200, )
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=mypass_img)
canvas.grid(row=0, column=1)

website_title = Label(text='Website:')
website_title.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)

email_title = Label(text='Email/Username:')
email_title.grid(row=2, column=0)

email_entry = Entry(width=38)
email_entry.insert(0, 'abc@gmail.com')
email_entry.grid(row=2, column=1,columnspan=2)

password_title = Label(text='Password:')
password_title.grid(row=3, column=0)

password_entry = Entry(width=21,)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=capture_info)
add_button.grid(row=4, column=1, columnspan=2)


















window.mainloop()