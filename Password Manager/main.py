from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password ():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list= password_numbers+password_symbols+password_letters

    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0 :
        messagebox.showinfo(title="OOPS",message="Please don't leave any field empty")
    else:
        is_ok=messagebox.askokcancel(title="Website" , message=f"These are details you entered : \n Email : {email} \nPassword: {password} \n Is it okay to save? ")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}        | {email}        | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50, bg="white", highlightthickness=0)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# Labels (Aligning to the right)
website_label = Label(text="Website :", anchor="e")
website_label.grid(row=1, column=0, sticky="E")

email_label = Label(text="Email/Username :", anchor="e")
email_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password :", anchor="e")
password_label.grid(row=3, column=0, sticky="E")


# Entries
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0,"abhi.sharma19jan@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="W")


# Buttons
generate_pass = Button(text="Generate Password",command=generate_password)
generate_pass.grid(row=3, column=2, padx=5)

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
