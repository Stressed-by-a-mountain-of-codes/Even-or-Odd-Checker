import tkinter as tk
from tkinter import messagebox
import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_even_odd(event=None):
    try:
        num = int(entry.get())
        if num % 2 == 0:
            result = f"{num} is Even ✅"
            color = "green"
            speak(f"{num} is even")
        else:
            result = f"{num} is Odd ❗"
            color = "blue"
            speak(f"{num} is odd")
        result_label.config(text=result, fg=color)
        root.after(3000, reset)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Even or Odd Checker + Voice")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()
entry.bind("<Return>", check_even_odd)

tk.Button(root, text="Check", font=("Arial", 12), command=check_even_odd).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

entry.focus()

root.mainloop()
