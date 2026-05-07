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
    

def check_guess():
    global attempts_left

    
    try:
        user_input = int(entry.get())
    except ValueError:
        feedback_label.config(text="Please enter a valid number.", fg="#FF6B9D")
        return
        
    if user_input == secret_number:
        feedback_label.config(text=f"Correct! The number was {secret_number}.", fg="#2E8B57")
        guess_button.config(state="disabled", bg="#A8E6CF", fg="#2E8B57")       
        entry.config(state="disabled")
    elif user_input < secret_number:
        feedback_label.config(text="Too low! Try again.", fg="#FF6B9D")      
        attempts_left -= 1
    else:
        feedback_label.config(text="Too high! Try again.", fg="#FF6B9D")    
        attempts_left -= 1

    
    update_attempts()

    
    if attempts_left <= 0 and guess_button["state"] != "disabled":
        feedback_label.config(text=f"Game over! The number was {secret_number}.", fg="#A00000")  
        guess_button.config(state="disabled")
        entry.config(state="disabled")
        
        


    
    
    
root.mainloop()