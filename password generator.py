import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return

    if length <= 0:
        messagebox.showerror("Invalid input", "Length must be greater than 0.")
        return

    chars = ''
    if letters_var.get():
        chars += string.ascii_letters
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Select options", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)

# Copy to clipboard
def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setup window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.configure(bg="#e0f7fa")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#e0f7fa").pack(pady=10)

# Length input
tk.Label(root, text="Password Length:", bg="#e0f7fa").pack()
length_entry = tk.Entry(root, justify='center')
length_entry.insert(0, "12")  # default length
length_entry.pack()

# Checkboxes
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

checkbox_frame = tk.Frame(root, bg="#e0f7fa")
checkbox_frame.pack(pady=10)

tk.Checkbutton(checkbox_frame, text="Letters", variable=letters_var, bg="#e0f7fa").grid(row=0, column=0, padx=10)
tk.Checkbutton(checkbox_frame, text="Digits", variable=digits_var, bg="#e0f7fa").grid(row=0, column=1, padx=10)
tk.Checkbutton(checkbox_frame, text="Symbols", variable=symbols_var, bg="#e0f7fa").grid(row=0, column=2, padx=10)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="#00796b", fg="white").pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#e0f7fa", fg="#004d40")
result_label.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#009688", fg="white").pack(pady=5)

# Run the app
root.mainloop()
