import tkinter as tk
from gui import run_gui 

def open_feedback_form(root, session):
    root.destroy()  # Close dashboard
    run_gui(session) # Open form

def run_dashboard(user_email):
    root = tk.Tk()
    root.title(f"Dashboard - {user_email}")
    root.geometry("800x600")
    
    # --- FLOWER THEME ---
    bg_color = "#FFFFFF"
    btn_color = "#FF69B4"
    text_color = "#000000"
    
    root.configure(bg=bg_color)

    sessions = [
        {"name": "AI Ethics 🤖", "date": "2025-11-20", "id": "S001"},
        {"name": "Urban Innovation 🏙️", "date": "2025-11-22", "id": "S002"},
        {"name": "Python Workshop 🐍", "date": "2025-11-24", "id": "S003"},
    ]

    tk.Label(root, text=f"🌺 Welcome, {user_email} 🌺", font=("Arial", 20, "bold"), 
             bg=bg_color, fg="#FF1493").pack(pady=20)

    tk.Label(root, text="Select a Session:", font=("Arial", 14), 
             bg=bg_color, fg=text_color).pack(pady=10)

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(pady=20)

    for i, session in enumerate(sessions):
        # Create a "Card" for each session
        card = tk.Frame(frame, bg="#FFF0F5", bd=2, relief="groove") # LavenderBlush background
        card.grid(row=i // 2, column=i % 2, padx=20, pady=20, ipadx=10, ipady=10)

        tk.Label(card, text=session['name'], font=("Arial", 14, "bold"), 
                 bg="#FFF0F5", fg=text_color).pack()
        
        tk.Label(card, text=session['date'], font=("Arial", 10), 
                 bg="#FFF0F5", fg="#555555").pack(pady=5)

        tk.Button(card, text="Give Feedback 🌷", bg=btn_color, fg="white", font=("Arial", 11, "bold"),
                  command=lambda s=session: open_feedback_form(root, s)).pack(pady=10)

    root.mainloop()
    return True # Just to satisfy main1 logic
