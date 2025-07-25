import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate the password
def create_password():
    user_input = length_entry.get()
    if not user_input.isdigit() or int(user_input) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return

    length = int(user_input)
    charset = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choices(charset, k=length))

    password_output.config(state='normal')
    password_output.delete(0, tk.END)
    password_output.insert(0, result)
    password_output.config(state='readonly')

# Function to copy password to clipboard
def copy_password():
    pwd = password_output.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Button hover effects
def on_enter(e):
    e.widget['background'] = '#555'

def on_leave(e):
    if e.widget == generate_btn:
        e.widget['background'] = '#4CAF50'
    else:
        e.widget['background'] = '#2196F3'

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x380")
root.configure(bg="#d3e3fc")
root.resizable(False, False)

# Card Frame
card = tk.Frame(root, bg="white", bd=2, relief="groove", padx=20, pady=20)
card.place(relx=0.5, rely=0.5, anchor='center')

# Title Label
title_label = tk.Label(
    card,
    text="🔐 Password Generator",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    fg="#333"
)
title_label.pack(pady=(0, 20))

# Password Length
length_frame = tk.Frame(card, bg="white")
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Password Length:", font=("Segoe UI", 12), bg="white")
length_label.pack(side="left", padx=5)

length_entry = tk.Entry(length_frame, font=("Segoe UI", 12), width=8, bd=2, relief="solid", justify="center")
length_entry.pack(side="left")

# Generate Button
generate_btn = tk.Button(
    card,
    text="Generate Password",
    font=("Segoe UI", 11),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    width=20,
    bd=0,
    cursor="hand2",
    command=create_password
)
generate_btn.pack(pady=15)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# Output Field
password_output = tk.Entry(card, font=("Courier", 12), width=36, justify="center", state='readonly', bd=2, relief="solid")
password_output.pack(pady=10)

# Copy Button
copy_btn = tk.Button(
    card,
    text="Copy to Clipboard",
    font=("Segoe UI", 11),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    width=20,
    bd=0,
    cursor="hand2",
    command=copy_password
)
copy_btn.pack(pady=10)
copy_btn.bind("<Enter>", on_enter)
copy_btn.bind("<Leave>", on_leave)

# Start GUI loop
root.mainloop()
