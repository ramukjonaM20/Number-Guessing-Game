# Import Libraries
import tkinter as tk
import random

# Class Definition
class GuessNumberGame:
    # Constructor Method
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        # Game Variables
        self.number = random.randint(1, 10)
        self.attempts = 3

        # Label for Instructions
        self.label = tk.Label(root, text="Guess the number between 1 and 10")
        self.label.pack()

        # Input Entry Box
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Attempts Tracking Label
        self.attempts_label = tk.Label(root, text=f"Remaining attempts: {self.attempts}")
        self.attempts_label.pack()

        # Submit Button
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack()

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

    # Check Guess Method
    def check_guess(self):
        # Try to Convert Input
        try:
            guess = int(self.entry.get())
            # Comparison and Feedback
            if guess < self.number:
                self.result_label.config(text="Too low!")
            elif guess > self.number:
                self.result_label.config(text="Too high!")
            else:
                self.result_label.config(text="Correct! You won!")
                self.button.config(state=tk.DISABLED)

            # Update Attempts
            self.attempts -= 1
            self.attempts_label.config(text=f"Remaining attempts: {self.attempts}")

            # Game Over Condition
            if self.attempts == 0:
                self.result_label.config(text=f"Game Over! The number was {self.number}.")
                self.button.config(state=tk.DISABLED)
        # Handle Invalid Input
        except ValueError:
            self.result_label.config(text="Please enter a valid number!")

    # Reset Game Method
    def reset_game(self):
        # Reset game variables
        self.number = random.randint(1, 10)
        self.attempts = 3
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempts_label.config(text=f"Remaining attempts: {self.attempts}")
        self.button.config(state=tk.NORMAL)

# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
