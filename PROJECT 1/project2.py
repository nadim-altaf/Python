import tkinter as tk
import random

# Game logic
def play(choice):
    options = {"snake": 1, "water": -1, "gun": 0}
    reverse = {1: "Snake", -1: "Water", 0: "Gun"}

    user = options[choice]
    computer = random.choice([-1, 0, 1])

    user_choice_label.config(text=f"You chose: {reverse[user]}")
    computer_choice_label.config(text=f"Computer chose: {reverse[computer]}")

    if user == computer:
        result_label.config(text="It's a Draw! 😐", fg="blue")
    elif (user == 1 and computer == -1) or \
         (user == -1 and computer == 0) or \
         (user == 0 and computer == 1):
        result_label.config(text="You Win! 🎉", fg="green")
    else:
        result_label.config(text="You Lose! 😢", fg="red")

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("300x300")
root.resizable(False, False)

# Labels
tk.Label(root, text="Choose one:", font=("Arial", 14)).pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Snake", width=10, command=lambda: play("snake")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water", width=10, command=lambda: play("water")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun", width=10, command=lambda: play("gun")).grid(row=0, column=2, padx=5)

# Output Labels
user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
