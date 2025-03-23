import tkinter as tk

# Function to switch to the second screen
def go_to_budget_screen():
    welcome_screen.pack_forget()  # Hide welcome screen
    budget_screen.pack()  # Show budget input screen

# Create the main window
root = tk.Tk()
root.title("Budget Buddy")
root.geometry("400x500")
root.configure(bg="#5e17eb")

# Welcome Screen
welcome_screen = tk.Frame(root, bg="#5e17eb")
welcome_screen.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_screen, text="WELCOME", font=("Arial", 18, "bold"), fg="white", bg="#5e17eb")
welcome_label.pack(pady=20)

app_name_label = tk.Label(welcome_screen, text="Budget Buddy", font=("Arial", 16, "bold"), fg="white", bg="#5e17eb")
app_name_label.pack(pady=10)

start_button = tk.Button(welcome_screen, text="START YOUR JOURNEY!", font=("Arial", 12, "bold"), 
                         bg="lightgray", command=go_to_budget_screen)
start_button.pack(pady=20)

# Budget Input Screen
budget_screen = tk.Frame(root, bg="#5e17eb")

title_label = tk.Label(budget_screen, text="Let's start your budgeting journey", 
                       font=("Arial", 16, "bold"), fg="white", bg="#5e17eb")
title_label.pack(pady=20)

title_entry = tk.Entry(budget_screen, width=30, font=("Arial", 12))
title_entry.insert(0, "Title")
title_entry.pack(pady=5)

duration_entry = tk.Entry(budget_screen, width=30, font=("Arial", 12))
duration_entry.insert(0, "Enter Duration")
duration_entry.pack(pady=5)

budget_entry = tk.Entry(budget_screen, width=30, font=("Arial", 12))
budget_entry.insert(0, "Enter Budget")
budget_entry.pack(pady=5)

submit_button = tk.Button(budget_screen, text="SUBMIT", font=("Arial", 12, "bold"), bg="lightgray")
submit_button.pack(pady=20)

# Start the application
root.mainloop()
