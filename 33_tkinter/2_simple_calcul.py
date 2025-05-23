import tkinter as tk


def cal_numbers():
    try:
        num1 = float(first_number.get())
        num2 = float(second_num.get())
        sum = num1 + num2
        result_label.config(text=f"Result {sum}")
    except ValueError:
        result_label.config(text="Please enter a valid number")


window = tk.Tk()
window.title("Tkinter Simple Calculator!")
window.geometry("450x300")

title_label = tk.Label(
    window, text="Welcome to simple claculater", font=("Arial", 15))
title_label.pack(pady=10)

frame1 = tk.Frame(window)
frame1.pack(pady=5)

num1_label = tk.Label(frame1, text="Enter First Num: ", font=("Arial", 10))
num1_label.pack(side=tk.LEFT)

first_number = tk.Entry(frame1, width=18)
first_number.pack()
first_number.focus()

frame2 = tk.Frame(window)
frame2.pack(pady=5)

num2_label = tk.Label(frame2, text="Enter Second Num: ", font=("Arial", 10))
num2_label.pack(side=tk.LEFT)

second_num = tk.Entry(frame2, width=18)
second_num.pack()


sum_button = tk.Button(window, text="Add Number", command=cal_numbers)
sum_button.pack(pady=10)

result_label = tk.Label(window, text="Result: ", font=("Arial", 10))
result_label.pack(pady=10)


def clear_fields():
    first_number.delete(0, tk.END)
    second_num.delete(0, tk.END)
    result_label.config(text="Result: ")


clear_button = tk.Button(window, text="Clear", font=(
    "Arial", 10), command=clear_fields)
clear_button.pack(pady=5)


window.mainloop()
