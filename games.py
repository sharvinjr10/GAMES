import tkinter as tk
from tkinter import messagebox
import random

class HigherLowerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Higher or Lower Game")
        
        self.current_number = random.randint(1, 100)
        self.next_number = None
        self.score = 0
        self.is_rolling = False
        
        # GUI Elements
        self.number_label = tk.Label(root, text=f"Current Number: {self.current_number}", font=("Arial", 24))
        self.number_label.pack(pady=20)
        
        self.next_label = tk.Label(root, text="Next Number: ?", font=("Arial", 20), fg="blue")
        self.next_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)
        
        # Buttons
        self.higher_button = tk.Button(root, text="HIGHER", command=self.start_roll_higher, 
                                      font=("Arial", 14), bg="green", fg="white", state=tk.NORMAL)
        self.higher_button.pack(pady=10, padx=20, ipadx=20)
        
        self.lower_button = tk.Button(root, text="LOWER", command=self.start_roll_lower, 
                                     font=("Arial", 14), bg="red", fg="white", state=tk.NORMAL)
        self.lower_button.pack(pady=10, padx=20, ipadx=20)
    
    def start_roll_higher(self):
        self.start_roll("higher")
    
    def start_roll_lower(self):
        self.start_roll("lower")
    
    def start_roll(self, guess):
        if self.is_rolling:
            return
        
        self.is_rolling = True
        self.user_guess = guess
        self.higher_button.config(state=tk.DISABLED)
        self.lower_button.config(state=tk.DISABLED)
        
        # Animation: Rapidly cycle numbers
        self.roll_count = 0
        self.roll_animation()
    
    def roll_animation(self):
        if self.roll_count < 15:  # Adjust for longer/shorter animation
            self.next_number = random.randint(1, 100)
            self.next_label.config(text=f"Next Number: {self.next_number}")
            self.root.after(100, self.roll_animation)  # Speed of animation (ms)
            self.roll_count += 1
        else:
            self.stop_roll()
    
    def stop_roll(self):
        self.is_rolling = False
        self.next_number = random.randint(1, 100)
        self.next_label.config(text=f"Next Number: {self.next_number}")
        
        # Check if guess was correct
        if (self.user_guess == "higher" and self.next_number > self.current_number) or \
           (self.user_guess == "lower" and self.next_number < self.current_number):
            self.score += 1
            self.current_number = self.next_number
            self.update_display()
        else:
            messagebox.showinfo("Game Over", f"Wrong! The number was {self.next_number}. Final Score: {self.score}")
            self.reset_game()
        
        # Re-enable buttons
        self.higher_button.config(state=tk.NORMAL)
        self.lower_button.config(state=tk.NORMAL)
    
    def update_display(self):
        self.number_label.config(text=f"Current Number: {self.current_number}")
        self.score_label.config(text=f"Score: {self.score}")
    
    def reset_game(self):
        self.current_number = random.randint(1, 100)
        self.score = 0
        self.next_label.config(text="Next Number: ?")
        self.update_display()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HigherLowerGame(root)
    root.mainloop()