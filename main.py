import tkinter as tk
import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("HelloBye - Password Generator")

# Create and place widgets
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

password_var = tk.StringVar()
password_var.set("Your generated password will appear here.")
password_label = tk.Label(root, textvariable=password_var, wraplength=300)
password_label.pack()

# Start the main event loop
root.mainloop()
