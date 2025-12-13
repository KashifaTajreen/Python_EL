'''import tkinter as tk
from tkinter import messagebox
from newaccount import open_create_account_window  # Import function from other file

from data import init_users_db, email_exists, create_account, validate_login

init_users_db()
#Global variable to store the logged in user
logged_in_user=None

def run_login():
    global logged_in_user
    logged_in_user=None #Reset
    
def submit_login():
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not email or not password:
        messagebox.showerror('Error', 'All fields are required.')
        return

    if validate_login(email, password):
        messagebox.showinfo('Success', 'Login successful!')
        # TODO: redirect to dashboard
    else:
        messagebox.showerror('Error', 'Invalid email or password.')

root = tk.Tk()
root.title('Login-Feedback Analyzer')
root.geometry('800x600')
bg_color='#FFFFFF'
btn_clor
root.configure(bg='#FFFFFF')

frame = tk.Frame(root, bg='#333333')
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Login", font=("Arial", 24, "bold"), bg='#333333', fg='#FF3399').grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(frame, text='Email', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
tk.Label(frame, text='Password', bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')

email_entry = tk.Entry(frame, width=40)
password_entry = tk.Entry(frame, width=40, show="*")

email_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(frame, text='Login', fg='#FFFFFF', bg='#FF3399',
          command=submit_login, font=("Arial", 14, "bold")).grid(row=3, column=1, pady=10)

tk.Button(frame, text='Create account', fg='#FFFFFF', bg='#FF3399',
          command=open_create_account_window, font=("Arial", 14, "bold")).grid(row=4, column=1, pady=20)

root.mainloop()'''

