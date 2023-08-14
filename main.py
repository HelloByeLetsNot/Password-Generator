import tkinter as tk
import random
import string
import webbrowser

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

def rick_roll():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Create the main window
root = tk.Tk()
root.title("HelloBye - Password Generator")
root.geometry("400x400") 
root.configure(bg="#f5f5f5")

# Variables
length_var = tk.StringVar(value="12")
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()
password_var.set("Your generated password will appear here.")

# Create and place widgets
tk.Label(root, text="Password Length:", bg="#f5f5f5", fg="#333333").pack(pady=5)
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack(pady=5)
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, bg="#f5f5f5", fg="#333333").pack(pady=5)
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#f5f5f5", fg="#333333").pack(pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var, bg="#f5f5f5", fg="#333333").pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click, bg="#007AFF", fg="white", padx=20, pady=10)
generate_button.pack(pady=10)

password_label = tk.Label(root, textvariable=password_var, wraplength=300, bg="#f5f5f5", fg="#333333")
password_label.pack(pady=10)

rick_roll_button = tk.Button(root, text="Surprise!", command=rick_roll, bg="#007AFF", fg="white", padx=20, pady=10)
rick_roll_button.pack(pady=20)

# Start the main event loop
root.mainloop()
