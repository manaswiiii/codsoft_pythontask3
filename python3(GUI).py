#password generator usig GUI

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.password_label.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError

            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            all_chars = letters + digits + special_chars

            password = ''.join(random.choice(all_chars) for _ in range(length))
            self.password_label.config(text=password)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
