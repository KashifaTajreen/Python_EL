import tkinter as tk
from tkinter import messagebox
from newaccount import open_create_account_window
from data import init_users_db, validate_login

# Initialize DB when this file loads
init_users_db()

# Global variable to store the logged-in user
logged_in_user = None

def run_login():
    global logged_in_user
    logged_in_user = None  # Reset

    root = tk.Tk()
    root.title("Login - 🌸 Feedback Analyzer 🌸")
    root.geometry("800x600")
    
    # --- FLOWER THEME ---
    bg_color = "#FFFFFF"       # White
    btn_color = "#FF69B4"      # Hot Pink
    text_color = "#000000"     # Black
    
    root.configure(bg=bg_color)

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(padx=20, pady=50)

    # Title with Flowers
    tk.Label(frame, text="🌸 Login 🌸", font=("Arial", 28, "bold"), 
             bg=bg_color, fg="#000000").grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(frame, text="Email", bg=bg_color, fg=text_color, 
             font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    tk.Label(frame, text="Password", bg=bg_color, fg=text_color, 
             font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')

    email_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    password_entry = tk.Entry(frame, width=30, show="*", font=("Arial", 12))

    email_entry.grid(row=1, column=1, padx=10, pady=10)
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    def submit_login():
        global logged_in_user
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if validate_login(email, password):
            messagebox.showinfo("Success", f"Welcome back, {email}! 🌺")
            logged_in_user = email # Save user
            root.destroy()         # Close window to proceed to dashboard
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    # Pink Buttons
    tk.Button(frame, text="Login", bg=btn_color, fg="white", 
              font=("Arial", 14, "bold"), command=submit_login).grid(row=3, column=1, pady=20, sticky="ew")

    tk.Button(frame, text="Create Account", bg="#FFB6C1", fg="black", # Lighter pink for secondary
              font=("Arial", 12), command=open_create_account_window).grid(row=4, column=1, pady=5, sticky="ew")

    root.mainloop()
    
    # Return the user back to main1.py
    return logged_in_user
