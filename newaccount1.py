'''import tkinter as tk
from tkinter import messagebox
import bcrypt
import sqlite3

sqlite3.connect("users.db")
def open_create_account_window():
    window = tk.Toplevel()
    window.title('Create Account')
    window.geometry('800x600')
    window.configure(bg='#333333')

    frame = tk.Frame(window, bg='#333333')
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Create Account", font=("Arial", 24, "bold"),
             bg='#333333', fg='#FF3399').grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(frame, text='Email', bg='#333333', fg='#FFFFFF',
             font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    tk.Label(frame, text='Password', bg='#333333', fg='#FFFFFF',
             font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    tk.Label(frame, text='Confirm Password', bg='#333333', fg='#FFFFFF',
             font=("Arial", 14, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky='w')

    email_entry = tk.Entry(frame, width=40)
    password_entry = tk.Entry(frame, width=40, show="*")
    confirm_password_entry = tk.Entry(frame, width=40, show="*")

    email_entry.grid(row=1, column=1, padx=10, pady=10)
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

    def submit_create_account():
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        confirm_password = confirm_password_entry.get().strip()

        if not email or not password or not confirm_password:
            messagebox.showerror('Error', 'All fields are required.')
            return

        if password != confirm_password:
            messagebox.showerror('Error', 'Passwords do not match.')
            return

        # Check if email already exists
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result:
            messagebox.showerror('Error', 'Email already exists. Please log in.')
        else:
            # Hash the password before saving
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                           (email, hashed_pw.decode('utf-8')))
            conn.commit()
            conn.close()

            messagebox.showinfo('Success', 'Account created successfully!')
            window.destroy()

    tk.Button(frame, text='Create account', fg='#FFFFFF', bg='#FF3399',
              command=submit_create_account, font=("Arial", 14, "bold")).grid(row=4, column=1, pady=20)'''



