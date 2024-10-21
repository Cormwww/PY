import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def greet_user():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for their name
    user_name = simpledialog.askstring("Input", "What is your name?")

    if user_name:
        # Display a greeting message
        messagebox.showinfo("Greeting", f"Hello, {user_name}!")
    else:
        # Handle the case where the user cancels or doesn't provide input
        messagebox.showinfo("Greeting", "Hello, Stranger!")

# Run the dialog
if __name__ == "__main__":
    greet_user()

