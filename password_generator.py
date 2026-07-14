import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a number.")


# Copy Password
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied!")


# Clear
def clear():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Password Generator",
                 font=("Arial", 18, "bold"))
title.pack(pady=15)

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root, width=15)
length_entry.pack(pady=5)

tk.Button(root,
          text="Generate Password",
          command=generate_password,
          bg="green",
          fg="white").pack(pady=10)

password_entry = tk.Entry(root,
                          width=35,
                          justify="center")
password_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame,
          text="Copy",
          command=copy_password,
          width=10).grid(row=0, column=0, padx=5)

tk.Button(button_frame,
          text="Clear",
          command=clear,
          width=10).grid(row=0, column=1, padx=5)

tk.Button(button_frame,
          text="Exit",
          command=root.destroy,
          width=10).grid(row=0, column=2, padx=5)

root.mainloop()