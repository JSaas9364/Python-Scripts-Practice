import tkinter as tk
from tkinter import messagebox

def fizz_buzz():
    try:
        user_in = int(entry.get())  # Get input from GUI Entry
        if user_in % 3 == 0 and user_in % 5 == 0:
            result.set("FizzBuzz")
        elif user_in % 3 == 0:
            result.set("Fizz")
        elif user_in % 5 == 0:
            result.set("Buzz")
        else:
            result.set("FizzBuzz")  # Show "FizzBuzz" instead of the number
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")  # Show error popup

# GUI Setup
root = tk.Tk()
root.title("FizzBuzz GUI")
root.geometry("300x200")  # Set window size

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Check FizzBuzz", font=("Arial", 14), command=fizz_buzz).pack(pady=10)

root.mainloop()
