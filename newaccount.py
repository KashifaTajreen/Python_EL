import tkinter as tk
from tkinter import messagebox
from data import create_account, email_exists

def open_create_account_window():
    window = tk.Toplevel()
    window.title("Create New Account")
    window.geometry("800x600")
    
    # --- BABY PINK & COZY THEME ---
    bg_color = "#FFF0F5"   # Lavender Blush (Very light baby pink)
    btn_color = "#FFC0CB"  # Pink (Lighter baby pink for buttons)
    text_color = "#4B0082" # Indigo/Dark Purple (Cozy contrast)

    window.configure(bg=bg_color)

    frame = tk.Frame(window, bg=bg_color)
    frame.pack(padx=30, pady=30)

    tk.Label(frame, text="✨ Register New Account ✨", font=("Arial", 18, "bold"), 
             bg=bg_color, fg=text_color).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Labels
    tk.Label(frame, text="Email:", bg=bg_color, fg=text_color, 
             font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    tk.Label(frame, text="Password:", bg=bg_color, fg=text_color, 
             font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')

    # Entries
    email_entry = tk.Entry(frame, width=30, font=("Arial", 11), bg="#FFFFFF")
    password_entry = tk.Entry(frame, width=30, show="*", font=("Arial", 11), bg="#FFFFFF")

    email_entry.grid(row=1, column=1, padx=10, pady=10)
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    def submit_create_account():
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if email_exists(email):
            messagebox.showerror("Error", "This email is already registered.")
            return

        try:
            create_account(email, password)
            messagebox.showinfo("Success", "Account created successfully! You can now log in. 💖")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    # Button
    tk.Button(frame, text="Create Account", fg=text_color, bg=btn_color,
              activebackground=bg_color, activeforeground=text_color,
              command=submit_create_account, font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=20, ipadx=10)

    window.mainloop()
