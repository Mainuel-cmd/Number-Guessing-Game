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
        
        
def restart_game():
    global secret_number, attempts_left

    secret_reservation = random.randint(1, 100)
    secret_number = secret_reservation
    attempts_left = 7
    update_attempts()
    feedback_label.config(text="Guess a number between 1 and 100.", fg="#2E8B57")  
    guess_button.config(state="normal", bg="#40E0D0", fg="white")
    entry.config(state="normal", bg="white", fg="black")
    entry.delete(0, tk.END)
    
    
title_label = tk.Label(
    root, text="Number Guessing Game",
    font=("Arial", 16, "bold"),
    bg="#B2F2BB", fg="#40E0D0"             
)
title_label.pack(pady=10)

instruction_label = tk.Label(
    root, text="Guess a number between 1 and 100:",
    bg="#B2F2BB", fg="#555555"             
)
instruction_label.pack()



entry = tk.Entry(root, font=("Arial", 12), width=20, bg="white", fg="#2E8B57")
entry.pack(pady=10)

guess_button = tk.Button(
    root, text="Guess! (*｀・ω-)ノ", command=check_guess,
    font=("Arial", 10, "bold"),
    bg="#40E0D0", fg="white", activebackground="#00CED1", activeforeground="white"
)
guess_button.pack(pady=5)

feedback_label = tk.Label(
    root, text="Guess a number between 1 and 100.",
    fg="#2E8B57", bg="#B2F2BB",
    font=("Arial", 10, "bold")
)
feedback_label.pack(pady=10)

attempts_label = tk.Label(
    root, text=f"Attempts left: {attempts_left}",
    font=("Arial", 10, "bold"), fg="#FF6B9D", bg="#B2F2BB"   
)
attempts_label.pack(pady=5)

restart_button = tk.Button(
    root, text="Restart Game (*ﾟ∀ﾟ)っ?", command=restart_game,
    font=("Arial", 10),
    bg="#FFB6C1", fg="white", activebackground="#FF6B9D"    
)
restart_button.pack(pady=10)
    
    
    
root.mainloop()