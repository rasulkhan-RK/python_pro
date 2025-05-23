import tkinter as tk


def say_hello():
    name = name_entry.get()
    message = f"Hello, {name}" if name else "Hello World"
    greeting_label.config(text=message)


window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("300x200")

title_label = tk.Label(window, text="Welcome to Tkinter!", font=("Arial", 15))
title_label.pack(pady=10)

name_entry = tk.Entry(window, width=20)
name_entry.pack(pady=10)
name_entry.focus()


hello_button = tk.Button(window, text="Say Hello", command=say_hello)
hello_button.pack(pady=10)


greeting_label = tk.Label(window, text="", font=("Arial", 13))
greeting_label.pack(pady=10)


window.mainloop()
