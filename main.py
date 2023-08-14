import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Function to generate a password."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """Function to determine password strength."""
    strength = "Weak"
    if len(password) >= 8:
        strength = "Medium"
        if any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in string.punctuation for c in password):
            strength = "Strong"
    return strength

def generate_button_click():
    """Function to handle the generate button click."""
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    password_var.set(password)
    strength_var.set(f"Strength: {password_strength(password)}")

def copy_password():
    """Function to copy password to clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def toggle_dark_mode():
    """Function to toggle dark mode."""
    if dark_mode_var.get():
        set_dark_mode()
    else:
        set_light_mode()

def set_dark_mode():
    """Function to apply dark mode."""
    root.configure(bg="black")
    password_label.configure(bg="black", fg="white")
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Checkbutton, tk.Button)):
            widget.configure(bg="black", fg="white")

def set_light_mode():
    """Function to apply light mode."""
    root.configure(bg="white")
    password_label.configure(bg="white", fg="black")
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Checkbutton, tk.Button)):
            widget.configure(bg="white", fg="black")

# Create the main window
root = tk.Tk()
root.title("HelloBye - Password Generator")

# <!-- UI Elements -->

tk.Label(root, text="Password Length:").pack()
length_var = tk.StringVar(value="12")
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack()

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()

special_chars_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

password_var = tk.StringVar()
password_var.set("Your generated password will appear here.")
password_label = tk.Label(root, textvariable=password_var, wraplength=300)
password_label.pack()

strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var)
strength_label.pack()

dark_mode_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Toggle Dark Mode", variable=dark_mode_var, command=toggle_dark_mode).pack()

# <!-- End of UI Elements -->

# Start the main event loop
root.mainloop()
