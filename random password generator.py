import string
import random
import tkinter as tk

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            password_result.config(text="Password length must be a positive integer.")
            return
    except ValueError:
        password_result.config(text="Please enter a valid password length.")
        return

    random.shuffle(characters)

    password = []

    for _ in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    password_result.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
title_label.pack(pady=20)

length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
length_label.pack()

length_entry = tk.Entry(root, font=("Helvetica", 12))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.pack(pady=10)

password_result = tk.Label(root, text="", font=("Helvetica", 12))
password_result.pack()

quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Helvetica", 12))
quit_button.pack(pady=10)

root.mainloop()
