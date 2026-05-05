import tkinter as tk
import random

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x330")
root.resizable(False, False)
root.configure(bg="#B2F2BB")   # this is a light mint‑teal background

secret_number = random.randint(1, 100)
attempts_left = 7
attempts_label = None

def update_attempts():
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    

    
    
    
root.mainloop()